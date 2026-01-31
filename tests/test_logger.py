"""
Tests for Logger Module

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2026
"""

import pytest
from hypothesis import given, strategies as st
from io import StringIO
import sys

from src.logger import HandbookLogger, Statistics, StatisticsCalculator
from src.placeholder_processor import ProcessingResult, Replacement


class TestStatisticsCalculator:
    """Tests for StatisticsCalculator."""
    
    def test_calculate_word_count_empty(self):
        """Test word count for empty content."""
        assert StatisticsCalculator.calculate_word_count("") == 0
        assert StatisticsCalculator.calculate_word_count("   ") == 0
    
    def test_calculate_word_count_simple(self):
        """Test word count for simple content."""
        content = "This is a test"
        assert StatisticsCalculator.calculate_word_count(content) == 4
    
    def test_calculate_word_count_multiline(self):
        """Test word count for multiline content."""
        content = """Line one has four words
Line two has four words"""
        # "Line", "one", "has", "four", "words", "Line", "two", "has", "four", "words" = 10 words
        assert StatisticsCalculator.calculate_word_count(content) == 10
    
    @given(st.text())
    def test_word_count_non_negative(self, content):
        """
        Feature: handbook-generator, Property 19: Statistics Calculation
        
        For any text content, word count should be non-negative.
        """
        word_count = StatisticsCalculator.calculate_word_count(content)
        assert word_count >= 0
    
    @given(st.lists(
        st.text(
            min_size=1, 
            alphabet=st.characters(
                blacklist_categories=('Cs', 'Cc', 'Zs', 'Zl', 'Zp'),
                min_codepoint=33  # Start from '!' to avoid whitespace
            )
        ), 
        min_size=1
    ))
    def test_word_count_matches_split(self, words):
        """
        Feature: handbook-generator, Property 19: Statistics Calculation
        
        For any list of non-whitespace words joined by single spaces, 
        word count should match list length.
        """
        # Filter out words that contain internal whitespace or are only whitespace
        non_empty_words = [w for w in words if w.strip() and ' ' not in w and '\t' not in w and '\n' not in w]
        if not non_empty_words:
            return  # Skip if all words are whitespace or contain spaces
        
        content = " ".join(non_empty_words)
        word_count = StatisticsCalculator.calculate_word_count(content)
        assert word_count == len(non_empty_words)


class TestStatisticsCalculation:
    """Property-based tests for statistics calculation."""
    
    @given(
        st.lists(
            st.builds(
                ProcessingResult,
                content=st.text(),
                replacements=st.lists(
                    st.builds(
                        Replacement,
                        placeholder=st.text(min_size=1),
                        value=st.text(),
                        source=st.text(min_size=1),
                        line_number=st.integers(min_value=1, max_value=1000)
                    ),
                    max_size=10
                ),
                warnings=st.lists(st.text(), max_size=5),
                errors=st.lists(st.text(), max_size=5)
            ),
            max_size=20
        ),
        st.text(),
        st.integers(min_value=0, max_value=1000000),
        st.floats(min_value=0.0, max_value=3600.0)
    )
    def test_statistics_calculation_properties(
        self,
        processed_results,
        output_content,
        output_size,
        processing_time
    ):
        """
        Feature: handbook-generator, Property 19: Statistics Calculation
        
        For any processing run, the system should calculate accurate statistics:
        - Document count matches number of processed results
        - Placeholder counts are non-negative
        - Word count is non-negative
        - Output size and processing time match inputs
        
        Validates: Requirements 10.2
        """
        stats = StatisticsCalculator.calculate_statistics(
            processed_results,
            output_content,
            output_size,
            processing_time
        )
        
        # Document count should match input
        assert stats.documents_processed == len(processed_results)
        
        # Placeholder counts should be non-negative
        assert stats.placeholders_replaced >= 0
        assert stats.placeholders_failed >= 0
        
        # Word count should be non-negative
        assert stats.total_words >= 0
        
        # Output size and processing time should match inputs
        assert stats.output_size_bytes == output_size
        assert stats.processing_time_seconds == processing_time
        
        # Replaced count should match sum of all replacements
        expected_replaced = sum(len(r.replacements) for r in processed_results)
        assert stats.placeholders_replaced == expected_replaced
    
    def test_statistics_with_failures(self):
        """Test statistics calculation with placeholder failures."""
        # Create results with warnings about failures
        result1 = ProcessingResult(
            content="test",
            replacements=[
                Replacement("{{ netbox.device }}", "server1", "netbox", 1)
            ],
            warnings=[
                "Line 2: Field 'missing_field' not found in data source 'netbox'",
                "Line 3: Unknown data source 'invalid' in placeholder"
            ]
        )
        
        result2 = ProcessingResult(
            content="test2",
            replacements=[],
            warnings=[
                "Line 1: Field 'another_missing' not found in data source 'netbox'"
            ]
        )
        
        stats = StatisticsCalculator.calculate_statistics(
            [result1, result2],
            "test output",
            100,
            1.5
        )
        
        assert stats.documents_processed == 2
        assert stats.placeholders_replaced == 1
        assert stats.placeholders_failed == 3  # Three warnings about failures


class TestHandbookLogger:
    """Tests for HandbookLogger."""
    
    def test_logger_initialization(self):
        """Test logger initialization."""
        logger = HandbookLogger(verbose=False)
        assert logger.verbose is False
        
        logger_verbose = HandbookLogger(verbose=True)
        assert logger_verbose.verbose is True
    
    def test_elapsed_time_not_started(self):
        """Test elapsed time when not started."""
        logger = HandbookLogger()
        assert logger.get_elapsed_time() == 0.0
    
    def test_elapsed_time_started(self):
        """Test elapsed time after starting."""
        import time
        logger = HandbookLogger()
        logger.start_processing()
        time.sleep(0.1)
        elapsed = logger.get_elapsed_time()
        assert elapsed >= 0.1
    
    def test_log_processing(self, capsys):
        """Test log_processing output."""
        logger = HandbookLogger()
        logger.log_processing("test_template.md")
        
        captured = capsys.readouterr()
        assert "Processing: test_template.md" in captured.out
    
    def test_log_replacement_normal_mode(self, capsys):
        """Test that replacements are not logged in normal mode."""
        logger = HandbookLogger(verbose=False)
        replacement = Replacement(
            placeholder="{{ netbox.device }}",
            value="server1",
            source="netbox",
            line_number=5
        )
        logger.log_replacement(replacement)
        
        captured = capsys.readouterr()
        assert captured.out == ""
    
    def test_log_replacement_verbose_mode(self, capsys):
        """Test that replacements are logged in verbose mode."""
        logger = HandbookLogger(verbose=True)
        replacement = Replacement(
            placeholder="{{ netbox.device }}",
            value="server1",
            source="netbox",
            line_number=5
        )
        logger.log_replacement(replacement)
        
        captured = capsys.readouterr()
        assert "[Line 5]" in captured.out
        assert "{{ netbox.device }}" in captured.out
        assert "server1" in captured.out
        assert "netbox" in captured.out
    
    def test_log_statistics(self, capsys):
        """Test statistics logging."""
        logger = HandbookLogger()
        stats = Statistics(
            documents_processed=5,
            placeholders_replaced=10,
            placeholders_failed=2,
            total_words=1500,
            output_size_bytes=8192,
            processing_time_seconds=2.5
        )
        logger.log_statistics(stats)
        
        captured = capsys.readouterr()
        assert "Processing Statistics" in captured.out
        assert "5" in captured.out  # documents
        assert "10" in captured.out  # replaced
        assert "2" in captured.out  # failed
        assert "1,500" in captured.out  # words
        assert "8,192" in captured.out  # bytes
        assert "2.50" in captured.out  # time
    
    def test_log_warning_normal_mode(self, capsys):
        """Test warning logging in normal mode."""
        logger = HandbookLogger(verbose=False)
        logger.log_warning("Test warning", "Verbose details")
        
        captured = capsys.readouterr()
        assert "WARNING: Test warning" in captured.err
        assert "Verbose details" not in captured.err
    
    def test_log_warning_verbose_mode(self, capsys):
        """Test warning logging in verbose mode."""
        logger = HandbookLogger(verbose=True)
        logger.log_warning("Test warning", "Verbose details")
        
        captured = capsys.readouterr()
        assert "WARNING: Test warning" in captured.err
        assert "Verbose details" in captured.err
    
    def test_log_error_normal_mode(self, capsys):
        """Test error logging in normal mode."""
        logger = HandbookLogger(verbose=False)
        logger.log_error("Test error", "Stack trace here")
        
        captured = capsys.readouterr()
        assert "ERROR: Test error" in captured.err
        assert "Stack trace here" not in captured.err
    
    def test_log_error_verbose_mode(self, capsys):
        """Test error logging in verbose mode."""
        logger = HandbookLogger(verbose=True)
        logger.log_error("Test error", "Stack trace here")
        
        captured = capsys.readouterr()
        assert "ERROR: Test error" in captured.err
        assert "Stack trace here" in captured.err
    
    def test_log_summary_no_issues(self, capsys):
        """Test summary with no warnings or errors."""
        logger = HandbookLogger()
        logger.log_summary([], [])
        
        captured = capsys.readouterr()
        assert "successfully" in captured.out
    
    def test_log_summary_with_issues(self, capsys):
        """Test summary with warnings and errors."""
        logger = HandbookLogger()
        warnings = ["Warning 1", "Warning 2"]
        errors = ["Error 1"]
        logger.log_summary(warnings, errors)
        
        captured = capsys.readouterr()
        assert "Processing Summary" in captured.out
        assert "Errors (1)" in captured.out
        assert "Warnings (2)" in captured.out
        assert "Error 1" in captured.out
        assert "Warning 1" in captured.out
        assert "Warning 2" in captured.out


class TestVerboseLogging:
    """Property-based tests for verbose logging."""
    
    def test_verbose_logging_detail_property(self):
        """
        Feature: handbook-generator, Property 20: Verbose Logging Detail
        
        For any placeholder replacement in verbose mode, the system should log:
        - Line number
        - Original placeholder
        - Replacement value
        - Data source
        
        Validates: Requirements 10.4, 10.5
        """
        @given(
            st.lists(
                st.builds(
                    Replacement,
                    placeholder=st.text(min_size=1, max_size=50),
                    value=st.text(max_size=100),
                    source=st.sampled_from(["netbox", "config", "manual"]),
                    line_number=st.integers(min_value=1, max_value=1000)
                ),
                min_size=1,
                max_size=20
            )
        )
        def check_verbose_logging(replacements):
            logger = HandbookLogger(verbose=True)
            
            # Capture output
            import io
            captured_output = io.StringIO()
            original_stdout = sys.stdout
            sys.stdout = captured_output
            
            try:
                for replacement in replacements:
                    logger.log_replacement(replacement)
                
                output = captured_output.getvalue()
                
                # Verify all replacements were logged
                for replacement in replacements:
                    assert f"[Line {replacement.line_number}]" in output
                    assert replacement.placeholder in output
                    assert replacement.value in output
                    assert replacement.source in output
            finally:
                sys.stdout = original_stdout
        
        check_verbose_logging()
    
    def test_verbose_mode_logs_replacements_property(self):
        """
        Feature: handbook-generator, Property 20: Verbose Logging Detail
        
        In verbose mode, all replacements should be logged.
        In normal mode, no replacements should be logged.
        
        Validates: Requirements 10.4, 10.5
        """
        @given(
            st.lists(
                st.builds(
                    Replacement,
                    placeholder=st.text(min_size=1),
                    value=st.text(),
                    source=st.text(min_size=1),
                    line_number=st.integers(min_value=1)
                ),
                max_size=10
            )
        )
        def check_verbose_vs_normal(replacements):
            import io
            
            # Test verbose mode
            logger_verbose = HandbookLogger(verbose=True)
            captured_verbose = io.StringIO()
            original_stdout = sys.stdout
            sys.stdout = captured_verbose
            
            try:
                for replacement in replacements:
                    logger_verbose.log_replacement(replacement)
                output_verbose = captured_verbose.getvalue()
            finally:
                sys.stdout = original_stdout
            
            # Test normal mode
            logger_normal = HandbookLogger(verbose=False)
            captured_normal = io.StringIO()
            sys.stdout = captured_normal
            
            try:
                for replacement in replacements:
                    logger_normal.log_replacement(replacement)
                output_normal = captured_normal.getvalue()
            finally:
                sys.stdout = original_stdout
            
            # Verbose mode should have output if there are replacements
            if replacements:
                assert len(output_verbose) > 0
            
            # Normal mode should have no output
            assert output_normal == ""
        
        check_verbose_vs_normal()
    
    def test_verbose_details_in_errors_property(self):
        """
        Feature: handbook-generator, Property 20: Verbose Logging Detail
        
        For any error with verbose details, verbose mode should show details
        while normal mode should not.
        
        Validates: Requirements 10.5
        """
        @given(
            st.text(min_size=1, max_size=100),
            st.text(min_size=1, max_size=200).filter(lambda x: x.strip())  # Ensure non-whitespace
        )
        def check_error_details(error_msg, verbose_details):
            # Skip if error_msg and verbose_details are the same or if verbose_details is substring of error_msg
            if error_msg == verbose_details or verbose_details in error_msg:
                return
            
            import io
            
            # Test verbose mode
            logger_verbose = HandbookLogger(verbose=True)
            captured_verbose = io.StringIO()
            original_stderr = sys.stderr
            sys.stderr = captured_verbose
            
            try:
                logger_verbose.log_error(error_msg, verbose_details)
                output_verbose = captured_verbose.getvalue()
            finally:
                sys.stderr = original_stderr
            
            # Test normal mode
            logger_normal = HandbookLogger(verbose=False)
            captured_normal = io.StringIO()
            sys.stderr = captured_normal
            
            try:
                logger_normal.log_error(error_msg, verbose_details)
                output_normal = captured_normal.getvalue()
            finally:
                sys.stderr = original_stderr
            
            # Both should show the main error
            assert error_msg in output_verbose
            assert error_msg in output_normal
            
            # Only verbose should show details (and they should be different from error_msg)
            assert verbose_details in output_verbose
            assert verbose_details not in output_normal
        
        check_error_details()



class TestErrorSummary:
    """Tests for error summary functionality."""
    
    @given(
        st.lists(st.text(min_size=1, max_size=100), min_size=0, max_size=20),
        st.lists(st.text(min_size=1, max_size=100), min_size=0, max_size=20)
    )
    def test_property_23_error_summary_completeness(self, warnings, errors):
        """
        Feature: handbook-generator, Property 23: Error Summary Completeness
        
        For any processing run with errors and warnings, the final summary should
        include all errors and warnings that occurred during processing.
        
        Validates: Requirements 12.5
        """
        import io
        
        logger = HandbookLogger()
        
        # Capture output
        captured_output = io.StringIO()
        original_stdout = sys.stdout
        sys.stdout = captured_output
        
        try:
            logger.log_summary(warnings, errors)
            output = captured_output.getvalue()
        finally:
            sys.stdout = original_stdout
        
        # If there are no warnings or errors, should show success message
        if not warnings and not errors:
            assert "successfully" in output.lower()
            return
        
        # Should show "Processing Summary" header
        assert "Processing Summary" in output
        
        # Should show error count if there are errors
        if errors:
            assert f"Errors ({len(errors)})" in output
            # All errors should be in the output
            for error in errors:
                assert error in output
        
        # Should show warning count if there are warnings
        if warnings:
            assert f"Warnings ({len(warnings)})" in output
            # All warnings should be in the output
            for warning in warnings:
                assert warning in output
        
        # Verify correct counts are displayed
        if errors:
            # Count how many times each error appears (should be exactly once)
            for error in errors:
                count = output.count(error)
                assert count >= 1, f"Error '{error}' should appear at least once in summary"
        
        if warnings:
            # Count how many times each warning appears (should be exactly once)
            for warning in warnings:
                count = output.count(warning)
                assert count >= 1, f"Warning '{warning}' should appear at least once in summary"
    
    def test_error_summary_with_multiple_errors(self, capsys):
        """Test error summary with multiple errors."""
        logger = HandbookLogger()
        
        errors = [
            "Template not found: backup.md",
            "API connection failed: timeout",
            "Invalid configuration: missing token"
        ]
        warnings = [
            "Placeholder not replaced: {{ netbox.device }}",
            "Template without numbering: readme.md"
        ]
        
        logger.log_summary(warnings, errors)
        
        captured = capsys.readouterr()
        
        # Verify all errors are present
        assert "Errors (3)" in captured.out
        for error in errors:
            assert error in captured.out
        
        # Verify all warnings are present
        assert "Warnings (2)" in captured.out
        for warning in warnings:
            assert warning in captured.out
    
    def test_error_summary_errors_only(self, capsys):
        """Test error summary with only errors."""
        logger = HandbookLogger()
        
        errors = ["Error 1", "Error 2"]
        warnings = []
        
        logger.log_summary(warnings, errors)
        
        captured = capsys.readouterr()
        
        assert "Errors (2)" in captured.out
        assert "Warnings" not in captured.out
        for error in errors:
            assert error in captured.out
    
    def test_error_summary_warnings_only(self, capsys):
        """Test error summary with only warnings."""
        logger = HandbookLogger()
        
        errors = []
        warnings = ["Warning 1", "Warning 2", "Warning 3"]
        
        logger.log_summary(warnings, errors)
        
        captured = capsys.readouterr()
        
        assert "Warnings (3)" in captured.out
        assert "Errors" not in captured.out
        for warning in warnings:
            assert warning in captured.out
    
    def test_error_summary_empty(self, capsys):
        """Test error summary with no errors or warnings."""
        logger = HandbookLogger()
        
        logger.log_summary([], [])
        
        captured = capsys.readouterr()
        
        assert "successfully" in captured.out.lower()
        assert "no warnings or errors" in captured.out.lower()
    
    def test_error_summary_preserves_order(self, capsys):
        """Test that error summary preserves order of errors and warnings."""
        logger = HandbookLogger()
        
        errors = ["First error", "Second error", "Third error"]
        warnings = ["First warning", "Second warning"]
        
        logger.log_summary(warnings, errors)
        
        captured = capsys.readouterr()
        output = captured.out
        
        # Find positions of errors
        error_positions = [output.find(error) for error in errors]
        # Verify they appear in order
        assert error_positions == sorted(error_positions)
        
        # Find positions of warnings
        warning_positions = [output.find(warning) for warning in warnings]
        # Verify they appear in order
        assert warning_positions == sorted(warning_positions)
    
    def test_error_summary_with_duplicate_messages(self, capsys):
        """Test error summary with duplicate error/warning messages."""
        logger = HandbookLogger()
        
        # Same error appears multiple times
        errors = ["Duplicate error", "Duplicate error", "Unique error"]
        warnings = ["Duplicate warning", "Duplicate warning"]
        
        logger.log_summary(warnings, errors)
        
        captured = capsys.readouterr()
        output = captured.out
        
        # Should show correct counts
        assert "Errors (3)" in output
        assert "Warnings (2)" in output
        
        # All messages should appear (even duplicates)
        assert output.count("Duplicate error") >= 2
        assert output.count("Duplicate warning") >= 2
        assert "Unique error" in output
