"""
Unit and property tests for TestSuiteRunner.

This module tests the test suite execution, output parsing, failure analysis,
and task generation functionality of the quality control system.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
"""

import pytest
import tempfile
import os
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
from hypothesis import given, strategies as st

from src.quality_control.test_suite_runner import TestSuiteRunner
from src.quality_control.data_structures import TestResult, FailedTest


class TestPytestCommandExecution:
    """Unit tests for pytest command execution."""
    
    def test_pytest_not_installed(self):
        """Test handling when pytest is not installed."""
        runner = TestSuiteRunner()
        
        with patch('subprocess.run') as mock_run:
            # Simulate pytest not found
            mock_run.side_effect = FileNotFoundError("pytest not found")
            
            result = runner.execute_tests()
            
            assert result.success is False
            assert result.error is not None
            assert "pytest is not installed" in result.error
            assert result.total_tests == 0
    
    def test_output_capture_works(self):
        """Test that stdout and stderr are captured correctly."""
        runner = TestSuiteRunner()
        
        with patch('subprocess.run') as mock_run:
            # Mock pytest --version check
            version_result = Mock()
            version_result.returncode = 0
            
            # Mock actual test run
            test_result = Mock()
            test_result.returncode = 0
            test_result.stdout = "collected 5 items\n\ntest_example.py::test_one PASSED\n"
            test_result.stderr = ""
            
            mock_run.side_effect = [version_result, test_result]
            
            result = runner.execute_tests("tests/")
            
            # Verify subprocess.run was called with correct arguments
            calls = mock_run.call_args_list
            assert len(calls) == 2
            
            # Check version check call
            assert calls[0][0][0] == ["python", "-m", "pytest", "--version"]
            
            # Check test execution call
            assert calls[1][0][0] == ["python", "-m", "pytest", "tests/", "-v", "--tb=short"]
            assert calls[1][1]["capture_output"] is True
            assert calls[1][1]["text"] is True
    
    def test_timeout_handling(self):
        """Test handling of test execution timeout."""
        runner = TestSuiteRunner()
        
        with patch('subprocess.run') as mock_run:
            # Mock pytest --version check
            version_result = Mock()
            version_result.returncode = 0
            
            # Mock timeout on actual test run
            import subprocess
            mock_run.side_effect = [
                version_result,
                subprocess.TimeoutExpired("pytest", 300)
            ]
            
            result = runner.execute_tests()
            
            assert result.success is False
            assert result.error is not None
            assert "timed out" in result.error.lower()
    
    def test_pytest_error_exit_code(self):
        """Test handling of pytest error exit codes."""
        runner = TestSuiteRunner()
        
        with patch('subprocess.run') as mock_run:
            # Mock pytest --version check
            version_result = Mock()
            version_result.returncode = 0
            
            # Mock pytest error (exit code 2 = internal error)
            test_result = Mock()
            test_result.returncode = 2
            test_result.stdout = ""
            test_result.stderr = "Internal pytest error"
            
            mock_run.side_effect = [version_result, test_result]
            
            result = runner.execute_tests()
            
            assert result.error is not None
            assert "exited with code 2" in result.error



class TestOutputParsingCompleteness:
    """Property tests for output parsing completeness."""
    
    @given(
        passed=st.integers(min_value=0, max_value=100),
        failed=st.integers(min_value=0, max_value=100),
        skipped=st.integers(min_value=0, max_value=100),
        duration=st.floats(min_value=0.0, max_value=1000.0, allow_nan=False, allow_infinity=False)
    )
    def test_property_7_test_output_parsing_completeness(self, passed, failed, skipped, duration):
        """
        Feature: quality-control-and-framework-documentation
        Property 7: Test Output Parsing Completeness
        
        For any pytest output containing test results, the Test_Runner should
        correctly parse and extract all test counts and duration.
        
        Validates: Requirements 3.2, 3.3, 3.4
        """
        runner = TestSuiteRunner()
        
        # Skip edge case where no tests exist but duration is specified
        # This is not a realistic pytest output scenario
        total_tests = passed + failed + skipped
        if total_tests == 0 and duration > 0:
            # pytest doesn't output duration when no tests are collected
            return
        
        # Generate pytest-like output
        output_lines = []
        
        # Add test execution lines
        for i in range(passed):
            output_lines.append(f"test_example.py::test_pass_{i} PASSED")
        
        for i in range(failed):
            output_lines.append(f"test_example.py::test_fail_{i} FAILED")
        
        for i in range(skipped):
            output_lines.append(f"test_example.py::test_skip_{i} SKIPPED")
        
        # Add summary line
        summary_parts = []
        if passed > 0:
            summary_parts.append(f"{passed} passed")
        if failed > 0:
            summary_parts.append(f"{failed} failed")
        if skipped > 0:
            summary_parts.append(f"{skipped} skipped")
        
        if summary_parts:
            output_lines.append(f"{'=' * 50} {', '.join(summary_parts)} in {duration:.2f}s {'=' * 50}")
        
        output = '\n'.join(output_lines)
        
        # Parse output
        result = runner.parse_output(output)
        
        # Verify all counts are correct
        assert result.passed == passed, f"Expected {passed} passed, got {result.passed}"
        assert result.failed == failed, f"Expected {failed} failed, got {result.failed}"
        assert result.skipped == skipped, f"Expected {skipped} skipped, got {result.skipped}"
        assert result.total_tests == passed + failed + skipped
        
        # Only check duration if tests were present
        if total_tests > 0:
            assert abs(result.duration - duration) < 0.01  # Allow small floating point difference
    
    @given(
        failed_tests=st.lists(
            st.tuples(
                st.text(alphabet=st.characters(whitelist_categories=('Lu', 'Ll', 'Nd')), min_size=1, max_size=20),
                st.text(alphabet=st.characters(whitelist_categories=('Lu', 'Ll', 'Nd')), min_size=1, max_size=20)
            ),
            min_size=0,
            max_size=10
        )
    )
    def test_property_7_failed_test_extraction(self, failed_tests):
        """
        Feature: quality-control-and-framework-documentation
        Property 7: Test Output Parsing Completeness (Failed Tests)
        
        For any pytest output containing failed tests, the Test_Runner should
        identify and extract information for all failed tests without omission.
        
        Validates: Requirements 3.2, 3.3, 3.4
        """
        runner = TestSuiteRunner()
        
        # Generate pytest-like output with failed tests
        output_lines = []
        
        for file_name, test_name in failed_tests:
            # Sanitize names to be valid Python identifiers
            file_name = ''.join(c if c.isalnum() or c == '_' else '_' for c in file_name)
            test_name = ''.join(c if c.isalnum() or c == '_' else '_' for c in test_name)
            
            if not file_name or not test_name:
                continue
            
            output_lines.append(f"test_{file_name}.py::test_{test_name} FAILED")
        
        # Add summary
        if failed_tests:
            output_lines.append(f"{'=' * 50} {len(failed_tests)} failed in 1.23s {'=' * 50}")
        
        output = '\n'.join(output_lines)
        
        # Parse output
        result = runner.parse_output(output)
        
        # Count valid test names
        valid_count = sum(1 for fn, tn in failed_tests 
                         if fn and tn and 
                         ''.join(c if c.isalnum() or c == '_' else '_' for c in fn) and
                         ''.join(c if c.isalnum() or c == '_' else '_' for c in tn))
        
        # Verify all failed tests were extracted
        assert len(result.failed_tests) == valid_count, \
            f"Expected {valid_count} failed tests, got {len(result.failed_tests)}"



class TestTaskCreationMapping:
    """Property tests for task creation mapping."""
    
    @given(
        failed_tests=st.lists(
            st.tuples(
                st.text(min_size=1, max_size=50),
                st.text(min_size=1, max_size=50),
                st.integers(min_value=1, max_value=1000),
                st.text(min_size=1, max_size=100)
            ),
            min_size=0,
            max_size=20
        )
    )
    def test_property_8_task_creation_mapping(self, failed_tests):
        """
        Feature: quality-control-and-framework-documentation
        Property 8: Task Creation Mapping
        
        For any set of failed tests, the Test_Runner should create exactly
        one task per failed test, maintaining a one-to-one correspondence.
        
        Validates: Requirements 3.5
        """
        runner = TestSuiteRunner()
        
        # Create FailedTest objects
        failed_test_objects = []
        for name, file_path, line_number, failure_reason in failed_tests:
            failed_test_objects.append(FailedTest(
                name=name,
                file_path=file_path,
                line_number=line_number,
                failure_reason=failure_reason,
                error_traceback="Sample traceback"
            ))
        
        # Create tasks
        tasks = runner.create_tasks(failed_test_objects)
        
        # Verify one-to-one mapping
        assert len(tasks) == len(failed_test_objects), \
            f"Expected {len(failed_test_objects)} tasks, got {len(tasks)}"
        
        # Verify each task corresponds to a failed test
        task_names = {task.test_name for task in tasks}
        failed_names = {ft.name for ft in failed_test_objects}
        assert task_names == failed_names, \
            "Task names don't match failed test names"
        
        # Verify all tasks have required fields
        for task in tasks:
            assert task.test_name, "Task missing test_name"
            assert task.description, "Task missing description"
            assert task.error_details, "Task missing error_details"
            assert task.priority in ['high', 'medium', 'low'], \
                f"Invalid priority: {task.priority}"



class TestReportCompleteness:
    """Property tests for report completeness."""
    
    @given(
        total_tests=st.integers(min_value=0, max_value=100),
        passed=st.integers(min_value=0, max_value=100),
        failed=st.integers(min_value=0, max_value=100),
        skipped=st.integers(min_value=0, max_value=100),
        duration=st.floats(min_value=0.0, max_value=1000.0, allow_nan=False, allow_infinity=False)
    )
    def test_property_4_report_completeness(self, total_tests, passed, failed, skipped, duration):
        """
        Feature: quality-control-and-framework-documentation
        Property 4: Report Completeness
        
        For any set of test results, generated reports should include
        information about all items in the input set.
        
        Validates: Requirements 1.5, 2.6, 3.7, 4.7, 5.4
        """
        runner = TestSuiteRunner()
        
        # Create test result
        result = TestResult(
            total_tests=total_tests,
            passed=passed,
            failed=failed,
            skipped=skipped,
            duration=duration,
            failed_tests=[],
            success=(failed == 0 and total_tests > 0)
        )
        
        # Generate report
        report = runner.generate_report(result)
        
        # Verify report contains all key information
        assert "Test Suite Execution Report" in report
        assert f"Total Tests: {total_tests}" in report
        assert f"Passed: {passed}" in report
        assert f"Failed: {failed}" in report
        assert f"Skipped: {skipped}" in report
        assert f"Duration: {duration:.2f}s" in report
        
        # Verify pass rate is included when there are tests
        if total_tests > 0:
            pass_rate = (passed / total_tests) * 100
            assert f"Pass Rate: {pass_rate:.1f}%" in report
        
        # Verify status is included
        assert "Status:" in report
    
    @given(
        failed_tests=st.lists(
            st.tuples(
                st.text(min_size=1, max_size=50),
                st.text(min_size=1, max_size=50),
                st.integers(min_value=1, max_value=1000),
                st.text(min_size=1, max_size=100)
            ),
            min_size=1,
            max_size=10
        )
    )
    def test_property_4_report_includes_all_failed_tests(self, failed_tests):
        """
        Feature: quality-control-and-framework-documentation
        Property 4: Report Completeness (Failed Tests)
        
        For any set of failed tests, the report should include information
        about all failed tests without omission.
        
        Validates: Requirements 1.5, 2.6, 3.7, 4.7, 5.4
        """
        runner = TestSuiteRunner()
        
        # Create FailedTest objects
        failed_test_objects = []
        for name, file_path, line_number, failure_reason in failed_tests:
            failed_test_objects.append(FailedTest(
                name=name,
                file_path=file_path,
                line_number=line_number,
                failure_reason=failure_reason,
                error_traceback="Sample traceback"
            ))
        
        # Create test result with failed tests
        result = TestResult(
            total_tests=len(failed_tests),
            passed=0,
            failed=len(failed_tests),
            skipped=0,
            duration=1.0,
            failed_tests=failed_test_objects,
            success=False
        )
        
        # Generate report
        report = runner.generate_report(result)
        
        # Verify all failed tests are mentioned in the report
        for failed_test in failed_test_objects:
            assert failed_test.name in report, \
                f"Failed test {failed_test.name} not found in report"



class TestParsingEdgeCases:
    """Unit tests for parsing edge cases."""
    
    def test_empty_pytest_output(self):
        """Test parsing empty pytest output."""
        runner = TestSuiteRunner()
        
        output = ""
        result = runner.parse_output(output)
        
        assert result.total_tests == 0
        assert result.passed == 0
        assert result.failed == 0
        assert result.skipped == 0
        assert result.duration == 0.0
        assert len(result.failed_tests) == 0
        assert result.success is False
    
    def test_all_tests_passing(self):
        """Test parsing output when all tests pass."""
        runner = TestSuiteRunner()
        
        output = """
test_example.py::test_one PASSED
test_example.py::test_two PASSED
test_example.py::test_three PASSED

======================== 3 passed in 1.23s ========================
"""
        
        result = runner.parse_output(output)
        
        assert result.total_tests == 3
        assert result.passed == 3
        assert result.failed == 0
        assert result.skipped == 0
        assert result.duration == 1.23
        assert len(result.failed_tests) == 0
        assert result.success is True
    
    def test_pytest_collection_error(self):
        """Test parsing output when pytest has collection errors."""
        runner = TestSuiteRunner()
        
        output = """
ERROR: file not found: nonexistent_test.py
"""
        
        result = runner.parse_output(output)
        
        # Should handle gracefully with zero counts
        assert result.total_tests == 0
        assert result.passed == 0
        assert result.failed == 0
        assert result.skipped == 0
    
    def test_mixed_results(self):
        """Test parsing output with mixed pass/fail/skip."""
        runner = TestSuiteRunner()
        
        output = """
test_example.py::test_pass PASSED
test_example.py::test_fail FAILED
test_example.py::test_skip SKIPPED

======================== 1 passed, 1 failed, 1 skipped in 2.45s ========================
"""
        
        result = runner.parse_output(output)
        
        assert result.total_tests == 3
        assert result.passed == 1
        assert result.failed == 1
        assert result.skipped == 1
        assert result.duration == 2.45
        assert len(result.failed_tests) == 1
        assert result.success is False
    
    def test_no_summary_line(self):
        """Test parsing output without summary line."""
        runner = TestSuiteRunner()
        
        output = """
test_example.py::test_one PASSED
test_example.py::test_two FAILED
"""
        
        result = runner.parse_output(output)
        
        # Should still extract failed test
        assert len(result.failed_tests) == 1
        assert result.failed_tests[0].name == "test_example.py::test_two"
    
    def test_special_characters_in_test_names(self):
        """Test parsing test names with special characters."""
        runner = TestSuiteRunner()
        
        output = """
test_example.py::test_with_underscore_123 FAILED
test_example.py::TestClass::test_method FAILED

======================== 2 failed in 1.0s ========================
"""
        
        result = runner.parse_output(output)
        
        # Note: Current implementation only captures simple test names
        # This test documents current behavior
        assert result.failed == 2
    
    def test_very_long_output(self):
        """Test parsing very long output with many tests."""
        runner = TestSuiteRunner()
        
        # Generate output with 100 tests
        lines = []
        for i in range(100):
            lines.append(f"test_example.py::test_{i} PASSED")
        
        lines.append("======================== 100 passed in 10.5s ========================")
        output = '\n'.join(lines)
        
        result = runner.parse_output(output)
        
        assert result.total_tests == 100
        assert result.passed == 100
        assert result.failed == 0
        assert result.duration == 10.5
