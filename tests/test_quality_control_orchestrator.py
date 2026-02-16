"""
Tests for Quality Control Orchestrator.

This module contains unit tests and property-based tests for the
QualityControlOrchestrator class.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

import pytest
import tempfile
import os
import json
import csv
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock
from hypothesis import given, strategies as st, settings
from datetime import datetime

from src.quality_control.quality_control_orchestrator import QualityControlOrchestrator
from src.quality_control.data_structures import (
    ValidationResult,
    VersionHistoryValidationResult,
    TestResult,
    Framework,
    QualityMetrics,
    QualityReport,
    FrameworkInfo,
    TemplateFile,
    FailedTest
)


class TestSequentialExecution:
    """Tests for sequential execution of validators."""
    
    @given(
        mapping_success=st.booleans(),
        version_success=st.booleans(),
        test_success=st.booleans()
    )
    @settings(max_examples=50)
    def test_property_sequential_execution(
        self,
        mapping_success,
        version_success,
        test_success
    ):
        """
        Feature: quality-control-and-framework-documentation
        Property 12: Sequential Execution
        
        For any quality control run, all validation checks should execute in
        the specified order (Framework Mapping → Version History → Test Suite
        → Coverage Documentation) regardless of individual check failures.
        
        **Validates: Requirements 5.1, 5.3**
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create minimal directory structure
            templates_de = Path(tmpdir) / "templates" / "de"
            templates_en = Path(tmpdir) / "templates" / "en"
            templates_de.mkdir(parents=True)
            templates_en.mkdir(parents=True)
            
            # Create orchestrator
            orchestrator = QualityControlOrchestrator(tmpdir)
            
            # Track execution order
            execution_order = []
            
            # Mock validators to track execution order
            original_mapping_validate = orchestrator.mapping_validator.validate
            original_version_validate = orchestrator.version_validator.validate
            original_test_validate = orchestrator.test_runner.validate
            original_coverage_discover = orchestrator.coverage_generator.discover_frameworks
            
            def mock_mapping_validate():
                execution_order.append('mapping')
                if mapping_success:
                    return ValidationResult(
                        total_frameworks=1,
                        valid_frameworks=1,
                        invalid_frameworks=[],
                        missing_files=[],
                        success=True
                    )
                else:
                    return ValidationResult(
                        total_frameworks=1,
                        valid_frameworks=0,
                        invalid_frameworks=[],
                        missing_files=[],
                        success=False
                    )
            
            def mock_version_validate():
                execution_order.append('version')
                if version_success:
                    return VersionHistoryValidationResult(
                        total_templates=1,
                        valid_templates=1,
                        missing_version_history=[],
                        invalid_format=[],
                        success=True
                    )
                else:
                    return VersionHistoryValidationResult(
                        total_templates=1,
                        valid_templates=0,
                        missing_version_history=[],
                        invalid_format=[],
                        success=False
                    )
            
            def mock_test_validate():
                execution_order.append('tests')
                if test_success:
                    return TestResult(
                        total_tests=10,
                        passed=10,
                        failed=0,
                        skipped=0,
                        duration=1.0,
                        failed_tests=[],
                        success=True
                    )
                else:
                    return TestResult(
                        total_tests=10,
                        passed=8,
                        failed=2,
                        skipped=0,
                        duration=1.0,
                        failed_tests=[],
                        success=False
                    )
            
            def mock_coverage_discover():
                execution_order.append('coverage')
                return []
            
            orchestrator.mapping_validator.validate = mock_mapping_validate
            orchestrator.version_validator.validate = mock_version_validate
            orchestrator.test_runner.validate = mock_test_validate
            orchestrator.coverage_generator.discover_frameworks = mock_coverage_discover
            
            # Execute all checks
            report = orchestrator.run_all_checks()
            
            # Property: All checks execute in correct order
            assert execution_order == ['mapping', 'version', 'tests', 'coverage'], \
                f"Checks did not execute in correct order. Got: {execution_order}"
            
            # Property: All checks execute even if some fail
            assert len(execution_order) == 4, \
                f"Not all checks executed. Expected 4, got {len(execution_order)}"
            
            # Property: Report contains results from all checks
            assert report.mapping_validation is not None
            assert report.version_validation is not None
            assert report.test_results is not None
            assert report.coverage_documentation is not None
    
    def test_sequential_execution_with_exceptions(self):
        """
        Test that execution continues even when validators raise exceptions.
        
        **Validates: Requirements 5.2, 5.3**
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            orchestrator = QualityControlOrchestrator(tmpdir)
            
            execution_order = []
            
            def mock_mapping_validate():
                execution_order.append('mapping')
                raise Exception("Mapping validation failed")
            
            def mock_version_validate():
                execution_order.append('version')
                return VersionHistoryValidationResult(
                    total_templates=1,
                    valid_templates=1,
                    missing_version_history=[],
                    invalid_format=[],
                    success=True
                )
            
            def mock_test_validate():
                execution_order.append('tests')
                raise Exception("Test execution failed")
            
            def mock_coverage_discover():
                execution_order.append('coverage')
                return []
            
            orchestrator.mapping_validator.validate = mock_mapping_validate
            orchestrator.version_validator.validate = mock_version_validate
            orchestrator.test_runner.validate = mock_test_validate
            orchestrator.coverage_generator.discover_frameworks = mock_coverage_discover
            
            # Execute all checks
            report = orchestrator.run_all_checks()
            
            # All checks should execute despite exceptions
            assert len(execution_order) == 4
            assert execution_order == ['mapping', 'version', 'tests', 'coverage']
            
            # Report should contain error information
            assert report.mapping_validation.error is not None
            assert report.test_results.error is not None
            
            # Successful checks should have valid results
            assert report.version_validation.success is True


class TestSpecificCheckExecution:
    """Tests for running specific checks."""
    
    def test_run_specific_check_mapping(self):
        """Test running only framework mapping validation."""
        with tempfile.TemporaryDirectory() as tmpdir:
            orchestrator = QualityControlOrchestrator(tmpdir)
            result = orchestrator.run_specific_check('mapping')
            assert isinstance(result, ValidationResult)
    
    def test_run_specific_check_version(self):
        """Test running only version history validation."""
        with tempfile.TemporaryDirectory() as tmpdir:
            orchestrator = QualityControlOrchestrator(tmpdir)
            result = orchestrator.run_specific_check('version')
            assert isinstance(result, VersionHistoryValidationResult)
    
    def test_run_specific_check_tests(self):
        """Test running only test suite."""
        with tempfile.TemporaryDirectory() as tmpdir:
            orchestrator = QualityControlOrchestrator(tmpdir)
            result = orchestrator.run_specific_check('tests')
            assert isinstance(result, TestResult)
    
    def test_run_specific_check_coverage(self):
        """Test running only coverage documentation."""
        with tempfile.TemporaryDirectory() as tmpdir:
            orchestrator = QualityControlOrchestrator(tmpdir)
            result = orchestrator.run_specific_check('coverage')
            assert isinstance(result, list)
    
    def test_run_specific_check_invalid_name(self):
        """Test that invalid check name raises ValueError."""
        with tempfile.TemporaryDirectory() as tmpdir:
            orchestrator = QualityControlOrchestrator(tmpdir)
            with pytest.raises(ValueError):
                orchestrator.run_specific_check('invalid_check')


class TestMetricsCalculation:
    """Tests for quality metrics calculation."""
    
    @given(
        total_frameworks=st.integers(min_value=1, max_value=100),
        valid_frameworks=st.integers(min_value=0, max_value=100),
        total_templates=st.integers(min_value=1, max_value=1000),
        valid_templates=st.integers(min_value=0, max_value=1000),
        total_tests=st.integers(min_value=1, max_value=500),
        passed_tests=st.integers(min_value=0, max_value=500),
        total_fw_count=st.integers(min_value=1, max_value=50),
        consistent_fw_count=st.integers(min_value=0, max_value=50)
    )
    @settings(max_examples=50)
    def test_property_metrics_calculation_completeness(
        self,
        total_frameworks,
        valid_frameworks,
        total_templates,
        valid_templates,
        total_tests,
        passed_tests,
        total_fw_count,
        consistent_fw_count
    ):
        """
        Feature: quality-control-and-framework-documentation
        Property 13: Metrics Calculation Completeness
        
        For any quality control run, all four quality metrics (framework mapping
        compliance, version history compliance, test pass rate, bilingual
        consistency rate) should be calculated and included in the report.
        
        **Validates: Requirements 8.1**
        """
        # Ensure valid_frameworks <= total_frameworks
        valid_frameworks = min(valid_frameworks, total_frameworks)
        # Ensure valid_templates <= total_templates
        valid_templates = min(valid_templates, total_templates)
        # Ensure passed_tests <= total_tests
        passed_tests = min(passed_tests, total_tests)
        # Ensure consistent_fw_count <= total_fw_count
        consistent_fw_count = min(consistent_fw_count, total_fw_count)
        
        with tempfile.TemporaryDirectory() as tmpdir:
            orchestrator = QualityControlOrchestrator(tmpdir)
            
            # Create mock validation results
            mapping_validation = ValidationResult(
                total_frameworks=total_frameworks,
                valid_frameworks=valid_frameworks,
                invalid_frameworks=[],
                missing_files=[],
                success=(valid_frameworks == total_frameworks)
            )
            
            version_validation = VersionHistoryValidationResult(
                total_templates=total_templates,
                valid_templates=valid_templates,
                missing_version_history=[],
                invalid_format=[],
                success=(valid_templates == total_templates)
            )
            
            test_results = TestResult(
                total_tests=total_tests,
                passed=passed_tests,
                failed=total_tests - passed_tests,
                skipped=0,
                duration=1.0,
                failed_tests=[],
                success=(passed_tests == total_tests)
            )
            
            # Create mock frameworks
            frameworks = []
            for i in range(total_fw_count):
                is_consistent = i < consistent_fw_count
                frameworks.append(Framework(
                    name=f"framework_{i}",
                    standard="Test Standard",
                    description="Test description",
                    template_count_de=10,
                    template_count_en=10 if is_consistent else 8,
                    path_de=Path(tmpdir),
                    path_en=Path(tmpdir),
                    bilingual_consistent=is_consistent
                ))
            
            # Calculate metrics
            metrics = orchestrator._calculate_metrics(
                mapping_validation,
                version_validation,
                test_results,
                frameworks
            )
            
            # Property: All four metrics are calculated
            assert hasattr(metrics, 'framework_mapping_compliance')
            assert hasattr(metrics, 'version_history_compliance')
            assert hasattr(metrics, 'test_pass_rate')
            assert hasattr(metrics, 'bilingual_consistency_rate')
            
            # Property: All metrics are non-negative percentages
            assert 0.0 <= metrics.framework_mapping_compliance <= 100.0
            assert 0.0 <= metrics.version_history_compliance <= 100.0
            assert 0.0 <= metrics.test_pass_rate <= 100.0
            assert 0.0 <= metrics.bilingual_consistency_rate <= 100.0
            
            # Property: Metrics are calculated correctly
            expected_mapping = (valid_frameworks / total_frameworks) * 100
            expected_version = (valid_templates / total_templates) * 100
            expected_test = (passed_tests / total_tests) * 100
            expected_bilingual = (consistent_fw_count / total_fw_count) * 100
            
            assert abs(metrics.framework_mapping_compliance - expected_mapping) < 0.01
            assert abs(metrics.version_history_compliance - expected_version) < 0.01
            assert abs(metrics.test_pass_rate - expected_test) < 0.01
            assert abs(metrics.bilingual_consistency_rate - expected_bilingual) < 0.01
    
    def test_metrics_calculation_with_zero_totals(self):
        """Test metrics calculation when totals are zero."""
        with tempfile.TemporaryDirectory() as tmpdir:
            orchestrator = QualityControlOrchestrator(tmpdir)
            
            # Create validation results with zero totals
            mapping_validation = ValidationResult(
                total_frameworks=0,
                valid_frameworks=0,
                invalid_frameworks=[],
                missing_files=[],
                success=True
            )
            
            version_validation = VersionHistoryValidationResult(
                total_templates=0,
                valid_templates=0,
                missing_version_history=[],
                invalid_format=[],
                success=True
            )
            
            test_results = TestResult(
                total_tests=0,
                passed=0,
                failed=0,
                skipped=0,
                duration=0.0,
                failed_tests=[],
                success=True
            )
            
            frameworks = []
            
            # Calculate metrics
            metrics = orchestrator._calculate_metrics(
                mapping_validation,
                version_validation,
                test_results,
                frameworks
            )
            
            # All metrics should be 0.0 when totals are zero
            assert metrics.framework_mapping_compliance == 0.0
            assert metrics.version_history_compliance == 0.0
            assert metrics.test_pass_rate == 0.0
            assert metrics.bilingual_consistency_rate == 0.0


class TestMetricsPersistence:
    """Tests for metrics persistence."""
    
    @given(
        num_runs=st.integers(min_value=1, max_value=10),
        compliance_values=st.lists(
            st.floats(min_value=0.0, max_value=100.0, allow_nan=False, allow_infinity=False),
            min_size=1,
            max_size=10
        )
    )
    @settings(max_examples=30)
    def test_property_metrics_persistence(self, num_runs, compliance_values):
        """
        Feature: quality-control-and-framework-documentation
        Property 14: Metrics Persistence
        
        For any calculated quality metrics, the system should persist them to
        the metrics history file with a timestamp.
        
        **Validates: Requirements 8.2**
        """
        # Ensure we have enough compliance values
        while len(compliance_values) < num_runs:
            compliance_values.append(50.0)
        
        with tempfile.TemporaryDirectory() as tmpdir:
            orchestrator = QualityControlOrchestrator(tmpdir)
            
            # Create and save multiple reports
            for i in range(num_runs):
                # Create a mock report
                metrics = QualityMetrics(
                    framework_mapping_compliance=compliance_values[i],
                    version_history_compliance=compliance_values[i],
                    test_pass_rate=compliance_values[i],
                    bilingual_consistency_rate=compliance_values[i]
                )
                
                report = QualityReport(
                    timestamp=datetime.now(),
                    mapping_validation=ValidationResult(
                        total_frameworks=10,
                        valid_frameworks=10,
                        invalid_frameworks=[],
                        missing_files=[],
                        success=True
                    ),
                    version_validation=VersionHistoryValidationResult(
                        total_templates=100,
                        valid_templates=100,
                        missing_version_history=[],
                        invalid_format=[],
                        success=True
                    ),
                    test_results=TestResult(
                        total_tests=50,
                        passed=50,
                        failed=0,
                        skipped=0,
                        duration=1.0,
                        failed_tests=[],
                        success=True
                    ),
                    coverage_documentation="Test documentation",
                    overall_success=True,
                    metrics=metrics,
                    execution_duration=1.0
                )
                
                # Save metrics
                orchestrator.save_metrics(report)
            
            # Property: Metrics history file exists
            assert orchestrator.metrics_history_file.exists()
            
            # Property: Metrics history file contains all runs
            with open(orchestrator.metrics_history_file, 'r') as f:
                history = json.load(f)
            
            assert "runs" in history
            assert len(history["runs"]) == num_runs
            
            # Property: Each run has all required fields
            for run in history["runs"]:
                assert "timestamp" in run
                assert "framework_mapping_compliance" in run
                assert "version_history_compliance" in run
                assert "test_pass_rate" in run
                assert "bilingual_consistency_rate" in run
                assert "total_frameworks" in run
                assert "total_templates" in run
                assert "total_tests" in run
                assert "execution_duration" in run
                assert "overall_success" in run
            
            # Property: Last run file exists and contains latest metrics
            assert orchestrator.last_run_file.exists()
            
            with open(orchestrator.last_run_file, 'r') as f:
                last_run = json.load(f)
            
            # Last run should match the last entry in history
            assert last_run["framework_mapping_compliance"] == history["runs"][-1]["framework_mapping_compliance"]
    
    def test_metrics_persistence_appends_to_existing(self):
        """Test that metrics are appended to existing history."""
        with tempfile.TemporaryDirectory() as tmpdir:
            orchestrator = QualityControlOrchestrator(tmpdir)
            
            # Create initial metrics history
            orchestrator.quality_dir.mkdir(parents=True, exist_ok=True)
            initial_history = {
                "runs": [
                    {
                        "timestamp": "2025-01-01T00:00:00",
                        "framework_mapping_compliance": 90.0,
                        "version_history_compliance": 85.0,
                        "test_pass_rate": 95.0,
                        "bilingual_consistency_rate": 100.0,
                        "total_frameworks": 10,
                        "total_templates": 100,
                        "total_tests": 50,
                        "execution_duration": 1.0,
                        "overall_success": True
                    }
                ]
            }
            
            with open(orchestrator.metrics_history_file, 'w') as f:
                json.dump(initial_history, f)
            
            # Create and save a new report
            metrics = QualityMetrics(
                framework_mapping_compliance=95.0,
                version_history_compliance=90.0,
                test_pass_rate=98.0,
                bilingual_consistency_rate=100.0
            )
            
            report = QualityReport(
                timestamp=datetime.now(),
                mapping_validation=ValidationResult(
                    total_frameworks=10,
                    valid_frameworks=10,
                    invalid_frameworks=[],
                    missing_files=[],
                    success=True
                ),
                version_validation=VersionHistoryValidationResult(
                    total_templates=100,
                    valid_templates=100,
                    missing_version_history=[],
                    invalid_format=[],
                    success=True
                ),
                test_results=TestResult(
                    total_tests=50,
                    passed=50,
                    failed=0,
                    skipped=0,
                    duration=1.0,
                    failed_tests=[],
                    success=True
                ),
                coverage_documentation="Test documentation",
                overall_success=True,
                metrics=metrics,
                execution_duration=1.0
            )
            
            orchestrator.save_metrics(report)
            
            # Load and verify history
            with open(orchestrator.metrics_history_file, 'r') as f:
                history = json.load(f)
            
            # Should have 2 runs now
            assert len(history["runs"]) == 2
            
            # First run should be unchanged
            assert history["runs"][0]["framework_mapping_compliance"] == 90.0
            
            # Second run should be the new one
            assert history["runs"][1]["framework_mapping_compliance"] == 95.0


class TestTrendAnalysis:
    """Tests for trend analysis."""
    
    @given(
        previous_value=st.floats(min_value=0.0, max_value=100.0, allow_nan=False, allow_infinity=False),
        current_value=st.floats(min_value=0.0, max_value=100.0, allow_nan=False, allow_infinity=False)
    )
    @settings(max_examples=50)
    def test_property_trend_detection(self, previous_value, current_value):
        """
        Feature: quality-control-and-framework-documentation
        Property 15: Trend Detection
        
        For any two consecutive quality control runs, the system should correctly
        identify whether each metric has improved, declined, or remained stable.
        
        **Validates: Requirements 8.3, 8.4, 8.5**
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            orchestrator = QualityControlOrchestrator(tmpdir)
            
            # Create previous run metrics
            orchestrator.quality_dir.mkdir(parents=True, exist_ok=True)
            previous_history = {
                "runs": [
                    {
                        "timestamp": "2025-01-01T00:00:00",
                        "framework_mapping_compliance": previous_value,
                        "version_history_compliance": previous_value,
                        "test_pass_rate": previous_value,
                        "bilingual_consistency_rate": previous_value,
                        "total_frameworks": 10,
                        "total_templates": 100,
                        "total_tests": 50,
                        "execution_duration": 1.0,
                        "overall_success": True
                    }
                ]
            }
            
            with open(orchestrator.metrics_history_file, 'w') as f:
                json.dump(previous_history, f)
            
            # Create current report
            current_metrics = QualityMetrics(
                framework_mapping_compliance=current_value,
                version_history_compliance=current_value,
                test_pass_rate=current_value,
                bilingual_consistency_rate=current_value
            )
            
            current_report = QualityReport(
                timestamp=datetime.now(),
                mapping_validation=ValidationResult(
                    total_frameworks=10,
                    valid_frameworks=10,
                    invalid_frameworks=[],
                    missing_files=[],
                    success=True
                ),
                version_validation=VersionHistoryValidationResult(
                    total_templates=100,
                    valid_templates=100,
                    missing_version_history=[],
                    invalid_format=[],
                    success=True
                ),
                test_results=TestResult(
                    total_tests=50,
                    passed=50,
                    failed=0,
                    skipped=0,
                    duration=1.0,
                    failed_tests=[],
                    success=True
                ),
                coverage_documentation="Test documentation",
                overall_success=True,
                metrics=current_metrics,
                execution_duration=1.0
            )
            
            # Analyze trends
            trends = orchestrator.analyze_trends(current_report)
            
            # Property: Trends are calculated for all metrics
            assert 'framework_mapping_compliance' in trends
            assert 'version_history_compliance' in trends
            assert 'test_pass_rate' in trends
            assert 'bilingual_consistency_rate' in trends
            
            # Property: Each trend has required fields
            for metric_name, trend_data in trends.items():
                assert 'current' in trend_data
                assert 'previous' in trend_data
                assert 'change' in trend_data
                assert 'trend' in trend_data
                
                # Property: Current and previous values match input
                assert abs(trend_data['current'] - current_value) < 0.01
                assert abs(trend_data['previous'] - previous_value) < 0.01
                
                # Property: Change is calculated correctly
                expected_change = current_value - previous_value
                assert abs(trend_data['change'] - expected_change) < 0.01
                
                # Property: Trend classification is correct
                if abs(expected_change) < 0.1:
                    assert trend_data['trend'] == 'stable'
                elif expected_change > 0:
                    assert trend_data['trend'] == 'improved'
                else:
                    assert trend_data['trend'] == 'declined'
    
    def test_trend_analysis_no_previous_data(self):
        """Test trend analysis when no previous data exists."""
        with tempfile.TemporaryDirectory() as tmpdir:
            orchestrator = QualityControlOrchestrator(tmpdir)
            
            current_report = QualityReport(
                timestamp=datetime.now(),
                mapping_validation=ValidationResult(
                    total_frameworks=10,
                    valid_frameworks=10,
                    invalid_frameworks=[],
                    missing_files=[],
                    success=True
                ),
                version_validation=VersionHistoryValidationResult(
                    total_templates=100,
                    valid_templates=100,
                    missing_version_history=[],
                    invalid_format=[],
                    success=True
                ),
                test_results=TestResult(
                    total_tests=50,
                    passed=50,
                    failed=0,
                    skipped=0,
                    duration=1.0,
                    failed_tests=[],
                    success=True
                ),
                coverage_documentation="Test documentation",
                overall_success=True,
                metrics=QualityMetrics(
                    framework_mapping_compliance=95.0,
                    version_history_compliance=90.0,
                    test_pass_rate=98.0,
                    bilingual_consistency_rate=100.0
                ),
                execution_duration=1.0
            )
            
            trends = orchestrator.analyze_trends(current_report)
            
            # Should return empty dict when no previous data
            assert trends == {}
    
    def test_trend_report_generation(self):
        """Test trend report generation."""
        with tempfile.TemporaryDirectory() as tmpdir:
            orchestrator = QualityControlOrchestrator(tmpdir)
            
            trends = {
                'framework_mapping_compliance': {
                    'current': 95.0,
                    'previous': 90.0,
                    'change': 5.0,
                    'trend': 'improved'
                },
                'version_history_compliance': {
                    'current': 85.0,
                    'previous': 90.0,
                    'change': -5.0,
                    'trend': 'declined'
                },
                'test_pass_rate': {
                    'current': 98.0,
                    'previous': 98.0,
                    'change': 0.0,
                    'trend': 'stable'
                },
                'bilingual_consistency_rate': {
                    'current': 100.0,
                    'previous': 100.0,
                    'change': 0.0,
                    'trend': 'stable'
                }
            }
            
            report = orchestrator.generate_trend_report(trends)
            
            # Report should contain key sections
            assert "IMPROVEMENTS" in report
            assert "REGRESSIONS" in report
            assert "STABLE" in report
            assert "Framework Mapping Compliance" in report
            assert "Version History Compliance" in report


class TestMetricsExport:
    """Tests for metrics export functionality."""
    
    @given(
        compliance_value=st.floats(min_value=0.0, max_value=100.0, allow_nan=False, allow_infinity=False),
        total_frameworks=st.integers(min_value=1, max_value=100),
        total_templates=st.integers(min_value=1, max_value=1000),
        total_tests=st.integers(min_value=1, max_value=500)
    )
    @settings(max_examples=30)
    def test_property_metrics_export_format(
        self,
        compliance_value,
        total_frameworks,
        total_templates,
        total_tests
    ):
        """
        Feature: quality-control-and-framework-documentation
        Property 16: Metrics Export Format
        
        For any quality metrics, the system should be able to export them in
        both JSON and CSV formats with all required fields present.
        
        **Validates: Requirements 8.7**
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            orchestrator = QualityControlOrchestrator(tmpdir)
            
            # Create a report
            metrics = QualityMetrics(
                framework_mapping_compliance=compliance_value,
                version_history_compliance=compliance_value,
                test_pass_rate=compliance_value,
                bilingual_consistency_rate=compliance_value
            )
            
            report = QualityReport(
                timestamp=datetime.now(),
                mapping_validation=ValidationResult(
                    total_frameworks=total_frameworks,
                    valid_frameworks=total_frameworks,
                    invalid_frameworks=[],
                    missing_files=[],
                    success=True
                ),
                version_validation=VersionHistoryValidationResult(
                    total_templates=total_templates,
                    valid_templates=total_templates,
                    missing_version_history=[],
                    invalid_format=[],
                    success=True
                ),
                test_results=TestResult(
                    total_tests=total_tests,
                    passed=total_tests,
                    failed=0,
                    skipped=0,
                    duration=1.0,
                    failed_tests=[],
                    success=True
                ),
                coverage_documentation="Test documentation",
                overall_success=True,
                metrics=metrics,
                execution_duration=1.0
            )
            
            # Export to JSON
            json_path = os.path.join(tmpdir, "metrics.json")
            orchestrator.export_metrics_json(report, json_path)
            
            # Property: JSON file exists
            assert os.path.exists(json_path)
            
            # Property: JSON file contains all required fields
            with open(json_path, 'r') as f:
                json_data = json.load(f)
            
            assert "timestamp" in json_data
            assert "execution_duration" in json_data
            assert "overall_success" in json_data
            assert "metrics" in json_data
            assert "details" in json_data
            
            # Property: Metrics section has all four metrics
            assert "framework_mapping_compliance" in json_data["metrics"]
            assert "version_history_compliance" in json_data["metrics"]
            assert "test_pass_rate" in json_data["metrics"]
            assert "bilingual_consistency_rate" in json_data["metrics"]
            
            # Property: Details section has all three subsections
            assert "framework_mapping" in json_data["details"]
            assert "version_history" in json_data["details"]
            assert "test_suite" in json_data["details"]
            
            # Property: Values match input
            assert abs(json_data["metrics"]["framework_mapping_compliance"] - compliance_value) < 0.01
            assert json_data["details"]["framework_mapping"]["total_frameworks"] == total_frameworks
            assert json_data["details"]["version_history"]["total_templates"] == total_templates
            assert json_data["details"]["test_suite"]["total_tests"] == total_tests
            
            # Export to CSV
            csv_path = os.path.join(tmpdir, "metrics.csv")
            orchestrator.export_metrics_csv(report, csv_path)
            
            # Property: CSV file exists
            assert os.path.exists(csv_path)
            
            # Property: CSV file contains all required fields
            with open(csv_path, 'r') as f:
                reader = csv.DictReader(f)
                rows = list(reader)
            
            assert len(rows) == 1
            row = rows[0]
            
            # Property: All required columns present
            required_columns = [
                'timestamp',
                'execution_duration',
                'overall_success',
                'framework_mapping_compliance',
                'version_history_compliance',
                'test_pass_rate',
                'bilingual_consistency_rate',
                'total_frameworks',
                'valid_frameworks',
                'total_templates',
                'valid_templates',
                'total_tests',
                'passed_tests',
                'failed_tests'
            ]
            
            for column in required_columns:
                assert column in row
            
            # Property: Values match input
            assert abs(float(row['framework_mapping_compliance']) - compliance_value) < 0.01
            assert int(row['total_frameworks']) == total_frameworks
            assert int(row['total_templates']) == total_templates
            assert int(row['total_tests']) == total_tests
    
    def test_csv_export_appends_to_existing(self):
        """Test that CSV export appends to existing file."""
        with tempfile.TemporaryDirectory() as tmpdir:
            orchestrator = QualityControlOrchestrator(tmpdir)
            csv_path = os.path.join(tmpdir, "metrics.csv")
            
            # Export first report
            report1 = QualityReport(
                timestamp=datetime.now(),
                mapping_validation=ValidationResult(
                    total_frameworks=10,
                    valid_frameworks=10,
                    invalid_frameworks=[],
                    missing_files=[],
                    success=True
                ),
                version_validation=VersionHistoryValidationResult(
                    total_templates=100,
                    valid_templates=100,
                    missing_version_history=[],
                    invalid_format=[],
                    success=True
                ),
                test_results=TestResult(
                    total_tests=50,
                    passed=50,
                    failed=0,
                    skipped=0,
                    duration=1.0,
                    failed_tests=[],
                    success=True
                ),
                coverage_documentation="Test documentation",
                overall_success=True,
                metrics=QualityMetrics(
                    framework_mapping_compliance=90.0,
                    version_history_compliance=85.0,
                    test_pass_rate=95.0,
                    bilingual_consistency_rate=100.0
                ),
                execution_duration=1.0
            )
            
            orchestrator.export_metrics_csv(report1, csv_path)
            
            # Export second report
            report2 = QualityReport(
                timestamp=datetime.now(),
                mapping_validation=ValidationResult(
                    total_frameworks=10,
                    valid_frameworks=10,
                    invalid_frameworks=[],
                    missing_files=[],
                    success=True
                ),
                version_validation=VersionHistoryValidationResult(
                    total_templates=100,
                    valid_templates=100,
                    missing_version_history=[],
                    invalid_format=[],
                    success=True
                ),
                test_results=TestResult(
                    total_tests=50,
                    passed=50,
                    failed=0,
                    skipped=0,
                    duration=1.0,
                    failed_tests=[],
                    success=True
                ),
                coverage_documentation="Test documentation",
                overall_success=True,
                metrics=QualityMetrics(
                    framework_mapping_compliance=95.0,
                    version_history_compliance=90.0,
                    test_pass_rate=98.0,
                    bilingual_consistency_rate=100.0
                ),
                execution_duration=1.0
            )
            
            orchestrator.export_metrics_csv(report2, csv_path)
            
            # Read CSV and verify both rows exist
            with open(csv_path, 'r') as f:
                reader = csv.DictReader(f)
                rows = list(reader)
            
            # Should have 2 rows
            assert len(rows) == 2
            
            # First row should have first report's values
            assert float(rows[0]['framework_mapping_compliance']) == 90.0
            
            # Second row should have second report's values
            assert float(rows[1]['framework_mapping_compliance']) == 95.0



class TestIntegration:
    """Integration tests for full orchestrator execution."""
    
    def test_full_orchestrator_execution(self):
        """
        Test full quality control orchestrator execution.
        
        **Validates: Requirements 5.1, 5.2, 5.3, 5.4**
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create minimal directory structure
            templates_de = Path(tmpdir) / "templates" / "de" / "test_framework"
            templates_en = Path(tmpdir) / "templates" / "en" / "test_framework"
            templates_de.mkdir(parents=True)
            templates_en.mkdir(parents=True)
            
            # Create a mapping file
            mapping_file = templates_de / "9999_Framework_Mapping.md"
            mapping_file.write_text("# Framework Mapping\n\nTest content")
            
            # Create a template with version history
            template_file = templates_de / "0010_Test_Template.md"
            template_file.write_text("""
# Test Template

## Version History

- Version 1.0 - Initial version
""")
            
            # Create orchestrator
            orchestrator = QualityControlOrchestrator(tmpdir)
            
            # Run all checks
            report = orchestrator.run_all_checks()
            
            # Verify report structure
            assert report is not None
            assert isinstance(report, QualityReport)
            assert report.timestamp is not None
            assert report.execution_duration > 0
            
            # Verify all validation results are present
            assert report.mapping_validation is not None
            assert report.version_validation is not None
            assert report.test_results is not None
            assert report.coverage_documentation is not None
            
            # Verify metrics are calculated
            assert report.metrics is not None
            assert hasattr(report.metrics, 'framework_mapping_compliance')
            assert hasattr(report.metrics, 'version_history_compliance')
            assert hasattr(report.metrics, 'test_pass_rate')
            assert hasattr(report.metrics, 'bilingual_consistency_rate')
            
            # Generate consolidated report
            consolidated_report = orchestrator.generate_consolidated_report(report)
            assert len(consolidated_report) > 0
            assert "QUALITY CONTROL CONSOLIDATED REPORT" in consolidated_report
            assert "QUALITY METRICS" in consolidated_report
    
    def test_full_orchestrator_with_multiple_frameworks(self):
        """
        Test orchestrator with multiple frameworks in both languages.
        
        **Validates: Requirements 5.1, 5.2, 5.3, 5.4**
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create multiple frameworks
            frameworks = ['bcm', 'isms', 'gdpr']
            
            for fw in frameworks:
                # German templates
                fw_de = Path(tmpdir) / "templates" / "de" / fw
                fw_de.mkdir(parents=True)
                (fw_de / "9999_Framework_Mapping.md").write_text(f"# {fw} Mapping")
                (fw_de / "0010_Template.md").write_text(f"# {fw}\n\n## Versionshistorie\n\n- Version 1.0")
                (fw_de / "0020_Template.md").write_text(f"# {fw}\n\n## Versionshistorie\n\n- Version 1.0")
                
                # English templates
                fw_en = Path(tmpdir) / "templates" / "en" / fw
                fw_en.mkdir(parents=True)
                (fw_en / "9999_Framework_Mapping.md").write_text(f"# {fw} Mapping")
                (fw_en / "0010_Template.md").write_text(f"# {fw}\n\n## Version History\n\n- Version 1.0")
                (fw_en / "0020_Template.md").write_text(f"# {fw}\n\n## Version History\n\n- Version 1.0")
            
            orchestrator = QualityControlOrchestrator(tmpdir)
            report = orchestrator.run_all_checks()
            
            # Verify all frameworks were discovered
            assert report.mapping_validation.total_frameworks >= len(frameworks) * 2
            
            # Verify all templates were scanned
            assert report.version_validation.total_templates >= len(frameworks) * 4
            
            # Verify bilingual consistency
            assert report.metrics.bilingual_consistency_rate >= 0.0
            
            # Generate and verify consolidated report
            consolidated_report = orchestrator.generate_consolidated_report(report)
            assert "FRAMEWORK MAPPING VALIDATION" in consolidated_report
            assert "VERSION HISTORY VALIDATION" in consolidated_report
    
    def test_orchestrator_with_failure_scenarios(self):
        """
        Test orchestrator execution with various failure scenarios.
        
        **Validates: Requirements 5.2, 5.3**
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create directory structure with issues
            templates_de = Path(tmpdir) / "templates" / "de" / "test_framework"
            templates_de.mkdir(parents=True)
            
            # No mapping file (will fail mapping validation)
            # No templates (will have empty version validation)
            
            orchestrator = QualityControlOrchestrator(tmpdir)
            
            # Run all checks - should continue despite failures
            report = orchestrator.run_all_checks()
            
            # Verify execution completed
            assert report is not None
            
            # Mapping validation should fail (no mapping file)
            assert not report.mapping_validation.success
            
            # Overall success should be False
            assert not report.overall_success
            
            # But all checks should have run
            assert report.version_validation is not None
            assert report.test_results is not None
            assert report.coverage_documentation is not None
    
    def test_orchestrator_with_mixed_success_failures(self):
        """
        Test orchestrator with some checks passing and some failing.
        
        **Validates: Requirements 5.2, 5.3**
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create framework with mapping file but no version history
            fw_de = Path(tmpdir) / "templates" / "de" / "test_framework"
            fw_de.mkdir(parents=True)
            
            # Has mapping file (will pass mapping validation)
            (fw_de / "9999_Framework_Mapping.md").write_text("# Mapping")
            
            # Has template without version history (will fail version validation)
            (fw_de / "0010_Template.md").write_text("# Template\n\nNo version history")
            
            orchestrator = QualityControlOrchestrator(tmpdir)
            report = orchestrator.run_all_checks()
            
            # Mapping validation should pass
            assert report.mapping_validation.success
            
            # Version validation should fail
            assert not report.version_validation.success
            
            # Overall should fail
            assert not report.overall_success
            
            # All checks should have results
            assert report.mapping_validation is not None
            assert report.version_validation is not None
            assert report.test_results is not None
            assert report.coverage_documentation is not None
    
    def test_orchestrator_with_bilingual_inconsistency(self):
        """
        Test orchestrator detecting bilingual inconsistencies.
        
        **Validates: Requirements 5.1, 5.2, 5.3, 5.4**
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create German framework with 3 templates
            fw_de = Path(tmpdir) / "templates" / "de" / "test_framework"
            fw_de.mkdir(parents=True)
            (fw_de / "9999_Framework_Mapping.md").write_text("# Mapping")
            (fw_de / "0010_Template.md").write_text("# T1\n\n## Versionshistorie\n\n- V1.0")
            (fw_de / "0020_Template.md").write_text("# T2\n\n## Versionshistorie\n\n- V1.0")
            (fw_de / "0030_Template.md").write_text("# T3\n\n## Versionshistorie\n\n- V1.0")
            
            # Create English framework with only 2 templates (inconsistent)
            fw_en = Path(tmpdir) / "templates" / "en" / "test_framework"
            fw_en.mkdir(parents=True)
            (fw_en / "9999_Framework_Mapping.md").write_text("# Mapping")
            (fw_en / "0010_Template.md").write_text("# T1\n\n## Version History\n\n- V1.0")
            (fw_en / "0020_Template.md").write_text("# T2\n\n## Version History\n\n- V1.0")
            
            orchestrator = QualityControlOrchestrator(tmpdir)
            report = orchestrator.run_all_checks()
            
            # Bilingual consistency should be less than 100%
            assert report.metrics.bilingual_consistency_rate < 100.0
            
            # Consolidated report should mention the inconsistency
            consolidated_report = orchestrator.generate_consolidated_report(report)
            assert "bilingual consistency" in consolidated_report.lower() or "Bilingual Consistency" in consolidated_report
    
    def test_metrics_tracking_over_multiple_runs(self):
        """
        Test metrics tracking over multiple quality control runs.
        
        **Validates: Requirements 5.4, 8.2, 8.3**
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create directory structure
            templates_de = Path(tmpdir) / "templates" / "de" / "test_framework"
            templates_de.mkdir(parents=True)
            
            # Create mapping file
            mapping_file = templates_de / "9999_Framework_Mapping.md"
            mapping_file.write_text("# Framework Mapping")
            
            orchestrator = QualityControlOrchestrator(tmpdir)
            
            # First run
            report1 = orchestrator.run_all_checks()
            orchestrator.save_metrics(report1)
            
            # Verify metrics were saved
            assert orchestrator.metrics_history_file.exists()
            
            # Second run
            report2 = orchestrator.run_all_checks()
            orchestrator.save_metrics(report2)
            
            # Load metrics history
            with open(orchestrator.metrics_history_file, 'r') as f:
                history = json.load(f)
            
            # Should have 2 runs
            assert len(history["runs"]) == 2
            
            # Analyze trends
            trends = orchestrator.analyze_trends(report2)
            
            # Trends should be calculated
            assert len(trends) > 0
            
            # Generate trend report
            trend_report = orchestrator.generate_trend_report(trends)
            assert len(trend_report) > 0
    
    def test_metrics_tracking_with_improvements(self):
        """
        Test metrics tracking showing improvements over time.
        
        **Validates: Requirements 8.2, 8.3, 8.4**
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create directory structure with two frameworks in both languages
            fw1_de = Path(tmpdir) / "templates" / "de" / "framework1"
            fw2_de = Path(tmpdir) / "templates" / "de" / "framework2"
            fw1_en = Path(tmpdir) / "templates" / "en" / "framework1"
            fw2_en = Path(tmpdir) / "templates" / "en" / "framework2"
            fw1_de.mkdir(parents=True)
            fw2_de.mkdir(parents=True)
            fw1_en.mkdir(parents=True)
            fw2_en.mkdir(parents=True)
            
            # First run - only one framework has mapping file (50% compliance)
            (fw1_de / "9999_Framework_Mapping.md").write_text("# Mapping")
            (fw1_en / "9999_Framework_Mapping.md").write_text("# Mapping")
            
            orchestrator = QualityControlOrchestrator(tmpdir)
            report1 = orchestrator.run_all_checks()
            orchestrator.save_metrics(report1)
            
            # Add mapping file to second framework for second run (100% compliance - improvement)
            (fw2_de / "9999_Framework_Mapping.md").write_text("# Mapping")
            (fw2_en / "9999_Framework_Mapping.md").write_text("# Mapping")
            
            # Second run - should show improvement
            report2 = orchestrator.run_all_checks()
            orchestrator.save_metrics(report2)
            
            # Analyze trends
            trends = orchestrator.analyze_trends(report2)
            
            # Framework mapping compliance should show improvement
            assert 'framework_mapping_compliance' in trends
            # Change should be positive (from 50% to 100%)
            assert trends['framework_mapping_compliance']['change'] > 0.1
            assert trends['framework_mapping_compliance']['trend'] == 'improved'
            
            # Generate trend report
            trend_report = orchestrator.generate_trend_report(trends)
            assert "IMPROVEMENTS" in trend_report or "IMPROVEMENT" in trend_report
            assert "Framework Mapping Compliance" in trend_report
    
    def test_metrics_tracking_with_regressions(self):
        """
        Test metrics tracking showing regressions over time.
        
        **Validates: Requirements 8.2, 8.3, 8.5**
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create directory structure with two frameworks in both languages
            fw1_de = Path(tmpdir) / "templates" / "de" / "framework1"
            fw2_de = Path(tmpdir) / "templates" / "de" / "framework2"
            fw1_en = Path(tmpdir) / "templates" / "en" / "framework1"
            fw2_en = Path(tmpdir) / "templates" / "en" / "framework2"
            fw1_de.mkdir(parents=True)
            fw2_de.mkdir(parents=True)
            fw1_en.mkdir(parents=True)
            fw2_en.mkdir(parents=True)
            
            # First run - both frameworks have mapping files (100% compliance)
            (fw1_de / "9999_Framework_Mapping.md").write_text("# Mapping")
            (fw2_de / "9999_Framework_Mapping.md").write_text("# Mapping")
            (fw1_en / "9999_Framework_Mapping.md").write_text("# Mapping")
            (fw2_en / "9999_Framework_Mapping.md").write_text("# Mapping")
            
            orchestrator = QualityControlOrchestrator(tmpdir)
            report1 = orchestrator.run_all_checks()
            orchestrator.save_metrics(report1)
            
            # Remove one mapping file for second run (50% compliance - regression)
            (fw2_de / "9999_Framework_Mapping.md").unlink()
            (fw2_en / "9999_Framework_Mapping.md").unlink()
            
            # Second run - should show regression
            report2 = orchestrator.run_all_checks()
            orchestrator.save_metrics(report2)
            
            # Analyze trends
            trends = orchestrator.analyze_trends(report2)
            
            # Framework mapping compliance should show decline
            assert 'framework_mapping_compliance' in trends
            # Change should be negative (from 100% to 50%)
            assert trends['framework_mapping_compliance']['change'] < -0.1
            assert trends['framework_mapping_compliance']['trend'] == 'declined'
            
            # Generate trend report
            trend_report = orchestrator.generate_trend_report(trends)
            assert "REGRESSIONS" in trend_report or "REGRESSION" in trend_report
    
    def test_full_workflow_with_exports(self):
        """
        Test complete workflow including execution, metrics saving, and exports.
        
        **Validates: Requirements 5.1, 5.4, 8.2, 8.7**
        """
        with tempfile.TemporaryDirectory() as tmpdir:
            # Create directory structure
            templates_de = Path(tmpdir) / "templates" / "de" / "test_framework"
            templates_de.mkdir(parents=True)
            
            # Create mapping file
            mapping_file = templates_de / "9999_Framework_Mapping.md"
            mapping_file.write_text("# Framework Mapping")
            
            # Create template with version history
            template_file = templates_de / "0010_Test.md"
            template_file.write_text("# Test\n\n## Version History\n\n- Version 1.0")
            
            orchestrator = QualityControlOrchestrator(tmpdir)
            
            # Run all checks
            report = orchestrator.run_all_checks()
            
            # Save metrics
            orchestrator.save_metrics(report)
            assert orchestrator.metrics_history_file.exists()
            assert orchestrator.last_run_file.exists()
            
            # Export to JSON
            json_path = os.path.join(tmpdir, "export", "metrics.json")
            orchestrator.export_metrics_json(report, json_path)
            assert os.path.exists(json_path)
            
            # Export to CSV
            csv_path = os.path.join(tmpdir, "export", "metrics.csv")
            orchestrator.export_metrics_csv(report, csv_path)
            assert os.path.exists(csv_path)
            
            # Generate consolidated report
            consolidated_report = orchestrator.generate_consolidated_report(report)
            assert "QUALITY CONTROL CONSOLIDATED REPORT" in consolidated_report
            
            # Verify JSON export content
            with open(json_path, 'r') as f:
                json_data = json.load(f)
            assert "metrics" in json_data
            assert "details" in json_data
            
            # Verify CSV export content
            with open(csv_path, 'r') as f:
                reader = csv.DictReader(f)
                rows = list(reader)
            assert len(rows) == 1
            assert "framework_mapping_compliance" in rows[0]
