"""
Quality Control System for Handbook Generator

This module provides comprehensive quality control validation for framework templates,
including framework mapping validation, version history validation, test suite execution,
and coverage documentation generation.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

from .data_structures import (
    FrameworkInfo,
    ValidationResult,
    TemplateFile,
    VersionHistoryValidationResult,
    TestResult,
    FailedTest,
    Task,
    Framework,
    TemplateCounts,
    ConsistencyReport,
    QualityReport,
    QualityMetrics,
)
from .base_validator import BaseValidator
from .framework_mapping_validator import FrameworkMappingValidator
from .version_history_validator import VersionHistoryValidator
from .test_suite_runner import TestSuiteRunner
from .interactive_mode import InteractiveMode
from .remediation_suggestions import RemediationSuggestions

__all__ = [
    "FrameworkInfo",
    "ValidationResult",
    "TemplateFile",
    "VersionHistoryValidationResult",
    "TestResult",
    "FailedTest",
    "Task",
    "Framework",
    "TemplateCounts",
    "ConsistencyReport",
    "QualityReport",
    "QualityMetrics",
    "BaseValidator",
    "FrameworkMappingValidator",
    "VersionHistoryValidator",
    "TestSuiteRunner",
    "InteractiveMode",
    "RemediationSuggestions",
]
