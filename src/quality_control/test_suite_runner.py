"""
Test Suite Runner for Quality Control System.

This module executes pytest test suites, parses output, analyzes failures,
and generates tasks for fixing failed tests.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
"""

import subprocess
import re
from typing import List, Optional
from pathlib import Path

from .base_validator import BaseValidator
from .data_structures import TestResult, FailedTest, Task


class TestSuiteRunner(BaseValidator):
    """
    Executes pytest test suite and analyzes results.
    
    This class runs pytest with verbose output, parses the results,
    identifies failed tests, and generates actionable tasks for fixes.
    """
    
    def __init__(self, test_path: str = "tests/"):
        """
        Initialize the test suite runner.
        
        Args:
            test_path: Path to the test directory (default: "tests/")
        """
        super().__init__()
        self.test_path = test_path
        
        # Define available test categories
        self.test_categories = {
            'unit': {
                'marker': 'not property and not slow and not integration',
                'description': 'Unit tests only (fast, isolated tests)',
                'timeout': 180
            },
            'integration': {
                'marker': 'integration',
                'description': 'Integration tests (component interaction)',
                'timeout': 300
            },
            'property': {
                'marker': 'property',
                'description': 'Property-based tests (Hypothesis)',
                'timeout': 600
            },
            'slow': {
                'marker': 'slow',
                'description': 'Slow tests (long-running)',
                'timeout': 600
            },
            'all': {
                'marker': None,
                'description': 'All tests (unit, integration, property, slow)',
                'timeout': 900
            }
        }
    
    def execute_tests(self, test_path: Optional[str] = None, category: str = 'unit') -> TestResult:
        """
        Execute pytest test suite and capture output.
        
        Args:
            test_path: Optional override for test directory path
            category: Test category to run ('unit', 'integration', 'property', 'slow', 'all')
            
        Returns:
            TestResult object containing execution results
        """
        path = test_path or self.test_path
        
        # Validate category
        if category not in self.test_categories:
            valid_categories = ', '.join(self.test_categories.keys())
            self.logger.error(f"Invalid test category: {category}. Valid categories: {valid_categories}")
            return TestResult(
                total_tests=0,
                passed=0,
                failed=0,
                skipped=0,
                duration=0.0,
                failed_tests=[],
                success=False,
                error=f"Invalid test category: {category}. Valid categories: {valid_categories}"
            )
        
        category_info = self.test_categories[category]
        
        # Check if pytest is available
        try:
            subprocess.run(
                ["python", "-m", "pytest", "--version"],
                capture_output=True,
                check=True,
                text=True
            )
        except (subprocess.CalledProcessError, FileNotFoundError) as e:
            self.logger.error("pytest is not installed or not accessible")
            return TestResult(
                total_tests=0,
                passed=0,
                failed=0,
                skipped=0,
                duration=0.0,
                failed_tests=[],
                success=False,
                error="pytest is not installed. Install with: pip install pytest"
            )
        
        # Execute pytest with verbose output
        try:
            self.logger.info(f"Executing pytest on {path}")
            self.logger.info(f"Test category: {category} - {category_info['description']}")
            
            if category != 'all':
                self.logger.info(f"Marker filter: {category_info['marker']}")
            
            print(f"\nRunning {category} test suite...")
            print(f"Description: {category_info['description']}")
            print("This may take a few minutes. Please wait...\n")
            
            # Build pytest command
            pytest_args = ["python", "-m", "pytest", path, "-v", "--tb=short"]
            
            # Add marker filter if not running all tests
            if category_info['marker']:
                pytest_args.extend(["-m", category_info['marker']])
            
            # Add maxfail for faster feedback (except for 'all' category)
            if category != 'all':
                pytest_args.append("--maxfail=10")
            
            result = subprocess.run(
                pytest_args,
                capture_output=True,
                text=True,
                timeout=category_info['timeout']
            )
            
            # Parse the output
            test_result = self.parse_output(result.stdout + "\n" + result.stderr)
            
            # Show summary immediately
            print(f"\nTest execution completed:")
            print(f"  Total: {test_result.total_tests}")
            print(f"  Passed: {test_result.passed}")
            print(f"  Failed: {test_result.failed}")
            print(f"  Skipped: {test_result.skipped}")
            print(f"  Duration: {test_result.duration:.2f}s\n")
            
            # pytest returns 0 for success, 1 for failures, other codes for errors
            if result.returncode not in [0, 1, 2]:  # 2 = interrupted (maxfail reached)
                test_result.error = f"pytest exited with code {result.returncode}"
            
            return test_result
            
        except subprocess.TimeoutExpired:
            timeout_minutes = category_info['timeout'] // 60
            self.logger.error(f"Test execution timed out after {timeout_minutes} minutes")
            return TestResult(
                total_tests=0,
                passed=0,
                failed=0,
                skipped=0,
                duration=0.0,
                failed_tests=[],
                success=False,
                error=f"Test execution timed out after {timeout_minutes} minutes"
            )
        except Exception as e:
            self.logger.error(f"Error executing tests: {e}")
            return TestResult(
                total_tests=0,
                passed=0,
                failed=0,
                skipped=0,
                duration=0.0,
                failed_tests=[],
                success=False,
                error=str(e)
            )
    
    def analyze_failures(self, result: TestResult) -> List[FailedTest]:
        """
        Analyze failed tests and categorize failures by type.
        
        Args:
            result: TestResult object containing failed tests
            
        Returns:
            List of FailedTest objects with categorized failures
        """
        categorized_failures = []
        
        for failed_test in result.failed_tests:
            # Categorize failure type based on error message
            failure_type = self._categorize_failure(failed_test.failure_reason)
            
            # Create enhanced FailedTest with category
            categorized_failures.append(FailedTest(
                name=failed_test.name,
                file_path=failed_test.file_path,
                line_number=failed_test.line_number,
                failure_reason=f"[{failure_type}] {failed_test.failure_reason}",
                error_traceback=failed_test.error_traceback
            ))
        
        return categorized_failures
    
    def _categorize_failure(self, failure_reason: str) -> str:
        """
        Categorize failure by type based on error message.
        
        Args:
            failure_reason: The failure reason string
            
        Returns:
            Category string (e.g., 'AssertionError', 'TypeError', 'ValueError')
        """
        failure_lower = failure_reason.lower()
        
        if 'assertionerror' in failure_lower or 'assert' in failure_lower:
            return 'AssertionError'
        elif 'typeerror' in failure_lower:
            return 'TypeError'
        elif 'valueerror' in failure_lower:
            return 'ValueError'
        elif 'keyerror' in failure_lower:
            return 'KeyError'
        elif 'attributeerror' in failure_lower:
            return 'AttributeError'
        elif 'importerror' in failure_lower or 'modulenotfounderror' in failure_lower:
            return 'ImportError'
        elif 'filenotfounderror' in failure_lower:
            return 'FileNotFoundError'
        elif 'permissionerror' in failure_lower:
            return 'PermissionError'
        elif 'timeout' in failure_lower:
            return 'TimeoutError'
        else:
            return 'UnknownError'
    
    def create_tasks(self, failures: List[FailedTest]) -> List[Task]:
        """
        Create Task objects for each failed test.
        
        Args:
            failures: List of FailedTest objects
            
        Returns:
            List of Task objects with one-to-one mapping to failed tests
        """
        tasks = []
        
        for failed_test in failures:
            # Determine priority based on failure type
            priority = self._determine_priority(failed_test.failure_reason)
            
            # Generate suggested fix based on failure type
            suggested_fix = self._generate_suggested_fix(failed_test)
            
            # Create task description
            description = f"Fix failing test: {failed_test.name}"
            
            tasks.append(Task(
                test_name=failed_test.name,
                description=description,
                error_details=f"{failed_test.failure_reason}\n\nTraceback:\n{failed_test.error_traceback}",
                priority=priority,
                suggested_fix=suggested_fix
            ))
        
        return tasks
    
    def _determine_priority(self, failure_reason: str) -> str:
        """
        Determine task priority based on failure type.
        
        Args:
            failure_reason: The failure reason string
            
        Returns:
            Priority level: 'high', 'medium', or 'low'
        """
        failure_lower = failure_reason.lower()
        
        # High priority: Import errors, syntax errors, critical failures
        if any(keyword in failure_lower for keyword in ['importerror', 'syntaxerror', 'modulenotfound', 'filenotfound']):
            return 'high'
        
        # Medium priority: Type errors, value errors, attribute errors
        if any(keyword in failure_lower for keyword in ['typeerror', 'valueerror', 'attributeerror', 'keyerror']):
            return 'medium'
        
        # Low priority: Assertion errors (test logic issues)
        return 'low'
    
    def _generate_suggested_fix(self, failed_test: FailedTest) -> str:
        """
        Generate suggested fix based on failure type.
        
        Args:
            failed_test: FailedTest object
            
        Returns:
            Suggested fix string
        """
        failure_lower = failed_test.failure_reason.lower()
        
        if 'importerror' in failure_lower or 'modulenotfound' in failure_lower:
            return "Check if the module is installed and the import path is correct. Run: pip install <missing-module>"
        
        elif 'filenotfound' in failure_lower:
            return "Verify the file path exists. Check if the file was moved or renamed."
        
        elif 'assertionerror' in failure_lower or 'assert' in failure_lower:
            return "Review the test assertion logic. Verify expected vs actual values."
        
        elif 'typeerror' in failure_lower:
            return "Check function arguments and types. Verify the correct number and type of arguments are passed."
        
        elif 'valueerror' in failure_lower:
            return "Verify input values are within expected ranges and formats."
        
        elif 'attributeerror' in failure_lower:
            return "Check if the object has the expected attribute. Verify object initialization."
        
        elif 'keyerror' in failure_lower:
            return "Verify the dictionary key exists. Check for typos in key names."
        
        else:
            return "Review the error traceback and test logic to identify the root cause."
    
    def validate(self) -> TestResult:
        """
        Execute validation by running the test suite.
        
        Returns:
            TestResult object
        """
        return self.execute_tests()
    
    def parse_output(self, output: str) -> TestResult:
        """
        Parse pytest verbose output to extract test results.
        
        Args:
            output: Combined stdout and stderr from pytest
            
        Returns:
            TestResult object with parsed information
        """
        failed_tests = []
        total_tests = 0
        passed = 0
        failed = 0
        skipped = 0
        duration = 0.0
        
        # Parse summary line: "5 passed, 2 failed, 1 skipped in 3.45s"
        # Also handle case where only duration is present: "in 3.45s"
        summary_pattern = r'(\d+)\s+passed|(\d+)\s+failed|(\d+)\s+skipped|in\s+([\d.]+)s'
        for match in re.finditer(summary_pattern, output):
            if match.group(1):
                passed = int(match.group(1))
            elif match.group(2):
                failed = int(match.group(2))
            elif match.group(3):
                skipped = int(match.group(3))
            elif match.group(4):
                duration = float(match.group(4))
        
        total_tests = passed + failed + skipped
        
        # Parse failed test details
        # Pattern: test_file.py::test_name FAILED or test_file.py::TestClass::test_name FAILED
        # Also handles parametrized tests: test_file.py::test_name[param] FAILED
        failed_pattern = r'([\w/]+\.py)::([\w:]+(?:\[[\w\s/\.\-]+\])?)\s+FAILED'
        failed_matches = re.finditer(failed_pattern, output)
        
        for match in failed_matches:
            file_path = match.group(1)
            test_name = match.group(2)
            
            # Extract failure details
            failure_reason, error_traceback, line_number = self._extract_failure_details(
                output, file_path, test_name
            )
            
            failed_tests.append(FailedTest(
                name=f"{file_path}::{test_name}",
                file_path=file_path,
                line_number=line_number,
                failure_reason=failure_reason,
                error_traceback=error_traceback
            ))
        
        success = failed == 0 and total_tests > 0
        
        return TestResult(
            total_tests=total_tests,
            passed=passed,
            failed=failed,
            skipped=skipped,
            duration=duration,
            failed_tests=failed_tests,
            success=success
        )
    
    def _extract_failure_details(self, output: str, file_path: str, test_name: str) -> tuple:
        """
        Extract failure reason and traceback for a specific test.
        
        Args:
            output: Full pytest output
            file_path: Path to test file
            test_name: Name of the test
            
        Returns:
            Tuple of (failure_reason, error_traceback, line_number)
        """
        # Look for the failure section for this test
        # Pattern: "_ test_name _" or "FAILED test_file.py::test_name"
        # Escape test_name since it may contain special regex characters (brackets, etc.)
        escaped_test_name = re.escape(test_name)
        test_section_pattern = rf'_{escaped_test_name}_|FAILED {re.escape(file_path)}::{escaped_test_name}'
        
        lines = output.split('\n')
        failure_start = -1
        
        for i, line in enumerate(lines):
            if re.search(test_section_pattern, line):
                failure_start = i
                break
        
        if failure_start == -1:
            return "Unknown failure", "", 0
        
        # Extract traceback and error message
        traceback_lines = []
        failure_reason = "Unknown failure"
        line_number = 0
        
        # Look for traceback starting from failure_start
        for i in range(failure_start, min(failure_start + 50, len(lines))):
            line = lines[i]
            
            # Extract line number from traceback
            line_match = re.search(r':(\d+):', line)
            if line_match and line_number == 0:
                line_number = int(line_match.group(1))
            
            # Look for assertion errors or exception messages
            if 'AssertionError' in line or 'Error:' in line or 'assert' in line:
                failure_reason = line.strip()
            
            # Collect traceback lines
            if line.strip() and not line.startswith('='):
                traceback_lines.append(line)
            
            # Stop at next test or end of section
            if i > failure_start and (line.startswith('_') or line.startswith('FAILED') or line.startswith('PASSED')):
                break
        
        error_traceback = '\n'.join(traceback_lines[:20])  # Limit to 20 lines
        
        return failure_reason, error_traceback, line_number
    
    def generate_report(self, result: TestResult) -> str:
        """
        Generate human-readable report from test results.
        
        Args:
            result: TestResult object
            
        Returns:
            Formatted report string
        """
        if result.error:
            return f"Test Suite Execution Failed\n{'=' * 50}\nError: {result.error}\n"
        
        report = []
        report.append("Test Suite Execution Report")
        report.append("=" * 50)
        report.append(f"Total Tests: {result.total_tests}")
        report.append(f"Passed: {result.passed}")
        report.append(f"Failed: {result.failed}")
        report.append(f"Skipped: {result.skipped}")
        report.append(f"Duration: {result.duration:.2f}s")
        
        if result.total_tests > 0:
            pass_rate = (result.passed / result.total_tests) * 100
            report.append(f"Pass Rate: {pass_rate:.1f}%")
        
        report.append(f"Status: {'PASSED' if result.success else 'FAILED'}")
        
        if result.failed_tests:
            report.append("\nFailed Tests:")
            report.append("-" * 50)
            for test in result.failed_tests:
                report.append(f"\n{test.name}")
                report.append(f"  File: {test.file_path}:{test.line_number}")
                report.append(f"  Reason: {test.failure_reason}")
        
        return "\n".join(report)
