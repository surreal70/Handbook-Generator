"""
Tests for CLI Framework Acceptance - Additional Compliance Frameworks

Tests that the CLI accepts the three new compliance frameworks:
- IDW PS 951 (German IT auditing standard)
- NIST CSF 2.0 (NIST Cybersecurity Framework)
- TOGAF (The Open Group Architecture Framework)

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2026
"""

import pytest
from hypothesis import given, settings, strategies as st
from pathlib import Path
from unittest.mock import patch
import sys

from src.cli import parse_arguments


class TestNewFrameworkCLIAcceptance:
    """Tests for CLI acceptance of new compliance frameworks."""
    
    def test_idw_ps_951_accepted_long_flag(self):
        """
        Test that 'idw-ps-951' framework is accepted with long flag.
        
        Validates: Requirements 6.7
        """
        test_args = [
            'cli.py',
            '--language', 'de',
            '--template', 'idw-ps-951'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == 'idw-ps-951'
        assert args.language == 'de'
    
    def test_idw_ps_951_accepted_short_flag(self):
        """
        Test that 'idw-ps-951' framework is accepted with short flag.
        
        Validates: Requirements 6.7
        """
        test_args = [
            'cli.py',
            '-l', 'de',
            '-t', 'idw-ps-951'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == 'idw-ps-951'
        assert args.language == 'de'
    
    def test_idw_ps_951_accepted_english(self):
        """
        Test that 'idw-ps-951' framework is accepted with English language.
        
        Validates: Requirements 6.7
        """
        test_args = [
            'cli.py',
            '--language', 'en',
            '--template', 'idw-ps-951'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == 'idw-ps-951'
        assert args.language == 'en'
    
    def test_nist_csf_accepted_long_flag(self):
        """
        Test that 'nist-csf' framework is accepted with long flag.
        
        Validates: Requirements 6.7
        """
        test_args = [
            'cli.py',
            '--language', 'en',
            '--template', 'nist-csf'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == 'nist-csf'
        assert args.language == 'en'
    
    def test_nist_csf_accepted_short_flag(self):
        """
        Test that 'nist-csf' framework is accepted with short flag.
        
        Validates: Requirements 6.7
        """
        test_args = [
            'cli.py',
            '-l', 'en',
            '-t', 'nist-csf'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == 'nist-csf'
        assert args.language == 'en'
    
    def test_nist_csf_accepted_german(self):
        """
        Test that 'nist-csf' framework is accepted with German language.
        
        Validates: Requirements 6.7
        """
        test_args = [
            'cli.py',
            '--language', 'de',
            '--template', 'nist-csf'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == 'nist-csf'
        assert args.language == 'de'
    
    def test_togaf_accepted_long_flag(self):
        """
        Test that 'togaf' framework is accepted with long flag.
        
        Validates: Requirements 6.7
        """
        test_args = [
            'cli.py',
            '--language', 'de',
            '--template', 'togaf'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == 'togaf'
        assert args.language == 'de'
    
    def test_togaf_accepted_short_flag(self):
        """
        Test that 'togaf' framework is accepted with short flag.
        
        Validates: Requirements 6.7
        """
        test_args = [
            'cli.py',
            '-l', 'de',
            '-t', 'togaf'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == 'togaf'
        assert args.language == 'de'
    
    def test_togaf_accepted_english(self):
        """
        Test that 'togaf' framework is accepted with English language.
        
        Validates: Requirements 6.7
        """
        test_args = [
            'cli.py',
            '--language', 'en',
            '--template', 'togaf'
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == 'togaf'
        assert args.language == 'en'
    
    def test_all_new_frameworks_with_both_languages(self):
        """
        Test that all new frameworks are accepted with both languages.
        
        Validates: Requirements 6.7
        """
        new_frameworks = ['idw-ps-951', 'nist-csf', 'togaf']
        languages = ['de', 'en']
        
        for framework in new_frameworks:
            for language in languages:
                test_args = [
                    'cli.py',
                    '--language', language,
                    '--template', framework
                ]
                
                with patch.object(sys, 'argv', test_args):
                    args = parse_arguments()
                
                assert args.template == framework, \
                    f"Framework '{framework}' should be accepted"
                assert args.language == language, \
                    f"Language '{language}' should be accepted"
    
    def test_new_frameworks_with_output_formats(self):
        """
        Test that new frameworks work with all output formats.
        
        Validates: Requirements 6.7
        """
        new_frameworks = ['idw-ps-951', 'nist-csf', 'togaf']
        output_formats = ['markdown', 'pdf', 'html', 'both', 'all']
        
        for framework in new_frameworks:
            for output_format in output_formats:
                test_args = [
                    'cli.py',
                    '--language', 'de',
                    '--template', framework,
                    '--output', output_format
                ]
                
                with patch.object(sys, 'argv', test_args):
                    args = parse_arguments()
                
                assert args.template == framework
                assert args.output == output_format
    
    def test_new_frameworks_with_verbose_flag(self):
        """
        Test that new frameworks work with verbose flag.
        
        Validates: Requirements 6.7
        """
        new_frameworks = ['idw-ps-951', 'nist-csf', 'togaf']
        
        for framework in new_frameworks:
            test_args = [
                'cli.py',
                '--language', 'en',
                '--template', framework,
                '--verbose'
            ]
            
            with patch.object(sys, 'argv', test_args):
                args = parse_arguments()
            
            assert args.template == framework
            assert args.verbose is True
    
    def test_new_frameworks_with_custom_config(self):
        """
        Test that new frameworks work with custom config file.
        
        Validates: Requirements 6.7
        """
        new_frameworks = ['idw-ps-951', 'nist-csf', 'togaf']
        
        for framework in new_frameworks:
            test_args = [
                'cli.py',
                '--language', 'de',
                '--template', framework,
                '--config', 'custom_config.yaml'
            ]
            
            with patch.object(sys, 'argv', test_args):
                args = parse_arguments()
            
            assert args.template == framework
            assert args.config == 'custom_config.yaml'
    
    def test_new_frameworks_with_custom_directories(self):
        """
        Test that new frameworks work with custom template and output directories.
        
        Validates: Requirements 6.7
        """
        new_frameworks = ['idw-ps-951', 'nist-csf', 'togaf']
        
        for framework in new_frameworks:
            test_args = [
                'cli.py',
                '--language', 'en',
                '--template', framework,
                '--template-dir', 'custom_templates',
                '--output-dir', 'custom_output'
            ]
            
            with patch.object(sys, 'argv', test_args):
                args = parse_arguments()
            
            assert args.template == framework
            assert args.template_dir == 'custom_templates'
            assert args.output_dir == 'custom_output'
    
    def test_new_frameworks_with_test_mode(self):
        """
        Test that new frameworks work with test mode flag.
        
        Validates: Requirements 6.7
        """
        new_frameworks = ['idw-ps-951', 'nist-csf', 'togaf']
        
        for framework in new_frameworks:
            test_args = [
                'cli.py',
                '--language', 'de',
                '--template', framework,
                '--test'
            ]
            
            with patch.object(sys, 'argv', test_args):
                args = parse_arguments()
            
            assert args.template == framework
            assert args.test is True
    
    def test_new_frameworks_with_separate_files(self):
        """
        Test that new frameworks work with separate files flag.
        
        Validates: Requirements 6.7
        """
        new_frameworks = ['idw-ps-951', 'nist-csf', 'togaf']
        
        for framework in new_frameworks:
            test_args = [
                'cli.py',
                '--language', 'en',
                '--template', framework,
                '--separate-files'
            ]
            
            with patch.object(sys, 'argv', test_args):
                args = parse_arguments()
            
            assert args.template == framework
            assert args.separate_files is True
    
    def test_new_frameworks_with_pdf_toc(self):
        """
        Test that new frameworks work with PDF TOC flag.
        
        Validates: Requirements 6.7
        """
        new_frameworks = ['idw-ps-951', 'nist-csf', 'togaf']
        
        for framework in new_frameworks:
            test_args = [
                'cli.py',
                '--language', 'de',
                '--template', framework,
                '--pdf-toc'
            ]
            
            with patch.object(sys, 'argv', test_args):
                args = parse_arguments()
            
            assert args.template == framework
            assert args.pdf_toc is True


class TestNewFrameworkCLIRejection:
    """Tests for CLI rejection of invalid framework names."""
    
    def test_invalid_framework_rejected(self):
        """
        Test that invalid framework names are rejected.
        
        Validates: Requirements 6.7
        """
        test_args = [
            'cli.py',
            '--language', 'de',
            '--template', 'invalid-framework'
        ]
        
        with patch.object(sys, 'argv', test_args):
            with pytest.raises(SystemExit) as exc_info:
                parse_arguments()
        
        # argparse exits with code 2 for invalid arguments
        assert exc_info.value.code == 2
    
    def test_typo_in_idw_ps_951_rejected(self):
        """
        Test that typos in 'idw-ps-951' are rejected.
        
        Validates: Requirements 6.7
        """
        typos = ['idw-ps-95', 'idw-951', 'idw-ps951', 'idwps951', 'idw_ps_951']
        
        for typo in typos:
            test_args = [
                'cli.py',
                '--language', 'de',
                '--template', typo
            ]
            
            with patch.object(sys, 'argv', test_args):
                with pytest.raises(SystemExit) as exc_info:
                    parse_arguments()
            
            assert exc_info.value.code == 2, \
                f"Typo '{typo}' should be rejected"
    
    def test_typo_in_nist_csf_rejected(self):
        """
        Test that typos in 'nist-csf' are rejected.
        
        Validates: Requirements 6.7
        """
        typos = ['nist-csf-2', 'nist-csf2', 'nistcsf', 'nist_csf', 'nist-cf']
        
        for typo in typos:
            test_args = [
                'cli.py',
                '--language', 'en',
                '--template', typo
            ]
            
            with patch.object(sys, 'argv', test_args):
                with pytest.raises(SystemExit) as exc_info:
                    parse_arguments()
            
            assert exc_info.value.code == 2, \
                f"Typo '{typo}' should be rejected"
    
    def test_typo_in_togaf_rejected(self):
        """
        Test that typos in 'togaf' are rejected.
        
        Validates: Requirements 6.7
        """
        typos = ['togaff', 'togf', 'toagf', 'togaf-adm', 'togaf9']
        
        for typo in typos:
            test_args = [
                'cli.py',
                '--language', 'de',
                '--template', typo
            ]
            
            with patch.object(sys, 'argv', test_args):
                with pytest.raises(SystemExit) as exc_info:
                    parse_arguments()
            
            assert exc_info.value.code == 2, \
                f"Typo '{typo}' should be rejected"


class TestNewFrameworkHelpText:
    """Tests for help text inclusion of new frameworks."""
    
    def test_idw_ps_951_in_help_text(self, capsys):
        """
        Test that 'idw-ps-951' appears in help text.
        
        Validates: Requirements 6.7
        """
        test_args = [
            'cli.py',
            '--help'
        ]
        
        with patch.object(sys, 'argv', test_args):
            with pytest.raises(SystemExit) as exc_info:
                parse_arguments()
        
        assert exc_info.value.code == 0
        
        captured = capsys.readouterr()
        help_output = captured.out.lower()
        
        assert 'idw-ps-951' in help_output
        assert 'idw ps 951' in help_output or 'it auditing' in help_output
    
    def test_nist_csf_in_help_text(self, capsys):
        """
        Test that 'nist-csf' appears in help text.
        
        Validates: Requirements 6.7
        """
        test_args = [
            'cli.py',
            '--help'
        ]
        
        with patch.object(sys, 'argv', test_args):
            with pytest.raises(SystemExit) as exc_info:
                parse_arguments()
        
        assert exc_info.value.code == 0
        
        captured = capsys.readouterr()
        help_output = captured.out.lower()
        
        assert 'nist-csf' in help_output
        assert 'cybersecurity framework' in help_output or 'nist csf' in help_output
    
    def test_togaf_in_help_text(self, capsys):
        """
        Test that 'togaf' appears in help text.
        
        Validates: Requirements 6.7
        """
        test_args = [
            'cli.py',
            '--help'
        ]
        
        with patch.object(sys, 'argv', test_args):
            with pytest.raises(SystemExit) as exc_info:
                parse_arguments()
        
        assert exc_info.value.code == 0
        
        captured = capsys.readouterr()
        help_output = captured.out.lower()
        
        assert 'togaf' in help_output
        assert 'enterprise architecture' in help_output or 'togaf' in help_output
    
    def test_all_new_frameworks_in_help_text(self, capsys):
        """
        Test that all new frameworks appear in help text.
        
        Validates: Requirements 6.7
        """
        test_args = [
            'cli.py',
            '--help'
        ]
        
        with patch.object(sys, 'argv', test_args):
            with pytest.raises(SystemExit) as exc_info:
                parse_arguments()
        
        assert exc_info.value.code == 0
        
        captured = capsys.readouterr()
        help_output = captured.out.lower()
        
        # All three new frameworks should appear
        assert 'idw-ps-951' in help_output
        assert 'nist-csf' in help_output
        assert 'togaf' in help_output
    
    def test_new_frameworks_in_examples(self, capsys):
        """
        Test that new frameworks appear in usage examples.
        
        Validates: Requirements 6.7
        """
        test_args = [
            'cli.py',
            '--help'
        ]
        
        with patch.object(sys, 'argv', test_args):
            with pytest.raises(SystemExit) as exc_info:
                parse_arguments()
        
        assert exc_info.value.code == 0
        
        captured = capsys.readouterr()
        help_output = captured.out.lower()
        
        # At least one new framework should appear in examples
        has_new_framework_example = (
            'idw-ps-951' in help_output or
            'nist-csf' in help_output or
            'togaf' in help_output
        )
        assert has_new_framework_example, \
            "At least one new framework should appear in usage examples"


class TestNewFrameworkPropertyBasedValidation:
    """Property-based tests for new framework CLI validation."""
    
    @settings(max_examples=100)
    @given(
        framework=st.sampled_from(['idw-ps-951', 'nist-csf', 'togaf']),
        language=st.sampled_from(['de', 'en']),
        output_format=st.sampled_from(['markdown', 'pdf', 'html', 'both', 'all'])
    )
    def test_property_new_frameworks_accepted(self, framework, language, output_format):
        """
        Feature: additional-compliance-frameworks
        Property: New Framework CLI Acceptance
        
        For any new framework (idw-ps-951, nist-csf, togaf) with any valid
        language and output format, the CLI SHALL accept the combination.
        
        Validates: Requirements 6.7
        """
        test_args = [
            'cli.py',
            '--language', language,
            '--template', framework,
            '--output', output_format
        ]
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == framework
        assert args.language == language
        assert args.output == output_format
    
    @settings(max_examples=50)
    @given(
        framework=st.sampled_from(['idw-ps-951', 'nist-csf', 'togaf']),
        verbose=st.booleans(),
        test_mode=st.booleans(),
        separate_files=st.booleans(),
        pdf_toc=st.booleans()
    )
    def test_property_new_frameworks_with_flags(self, framework, verbose, test_mode, separate_files, pdf_toc):
        """
        Feature: additional-compliance-frameworks
        Property: New Framework CLI Flag Combinations
        
        For any new framework with any combination of boolean flags,
        the CLI SHALL accept the combination.
        
        Validates: Requirements 6.7
        """
        test_args = ['cli.py', '--language', 'de', '--template', framework]
        
        if verbose:
            test_args.append('--verbose')
        if test_mode:
            test_args.append('--test')
        if separate_files:
            test_args.append('--separate-files')
        if pdf_toc:
            test_args.append('--pdf-toc')
        
        with patch.object(sys, 'argv', test_args):
            args = parse_arguments()
        
        assert args.template == framework
        assert args.verbose == verbose
        assert args.test == test_mode
        assert args.separate_files == separate_files
        assert args.pdf_toc == pdf_toc
