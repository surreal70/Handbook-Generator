"""
Framework Mapping Validator for Quality Control System.

This module validates that all framework directories contain properly named
mapping files (9999_Framework_Mapping.md) and reports any violations.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
"""

import os
from pathlib import Path
from typing import List
import logging

from .base_validator import BaseValidator
from .data_structures import FrameworkInfo, ValidationResult


class FrameworkMappingValidator(BaseValidator):
    """
    Validator for framework mapping file standardization.
    
    Ensures all framework directories contain properly named mapping files
    (9999_Framework_Mapping.md) and reports any missing or incorrectly named files.
    """
    
    EXPECTED_MAPPING_FILE = "9999_Framework_Mapping.md"
    
    def __init__(self, base_path: str = "."):
        """
        Initialize the Framework Mapping Validator.
        
        Args:
            base_path: Base path of the project (default: current directory)
        """
        super().__init__()
        self.base_path = Path(base_path)
        self.logger = logging.getLogger(__name__)
    
    def scan_frameworks(self, base_path: str = None) -> List[FrameworkInfo]:
        """
        Discover all framework directories under templates/de/ and templates/en/.
        
        Args:
            base_path: Optional base path override
            
        Returns:
            List of FrameworkInfo objects for all discovered frameworks
        """
        if base_path:
            search_path = Path(base_path)
        else:
            search_path = self.base_path
        
        frameworks = []
        
        # Scan both German and English template directories
        for language in ['de', 'en']:
            templates_dir = search_path / 'templates' / language
            
            if not templates_dir.exists():
                self.logger.warning(f"Templates directory not found: {templates_dir}")
                continue
            
            if not templates_dir.is_dir():
                self.logger.warning(f"Templates path is not a directory: {templates_dir}")
                continue
            
            # Scan for framework subdirectories
            try:
                for item in templates_dir.iterdir():
                    if item.is_dir():
                        # Check for mapping file
                        mapping_file_path = item / self.EXPECTED_MAPPING_FILE
                        has_mapping = mapping_file_path.exists()
                        
                        # Check for any mapping file (correct or incorrect name)
                        mapping_file_name = None
                        if has_mapping:
                            mapping_file_name = self.EXPECTED_MAPPING_FILE
                        else:
                            # Look for incorrectly named mapping files
                            for file in item.iterdir():
                                if file.is_file() and 'mapping' in file.name.lower():
                                    mapping_file_name = file.name
                                    break
                        
                        framework_info = FrameworkInfo(
                            name=item.name,
                            language=language,
                            path=item,
                            has_mapping_file=has_mapping,
                            mapping_file_name=mapping_file_name
                        )
                        frameworks.append(framework_info)
            except PermissionError as e:
                self.logger.error(f"Permission denied accessing {templates_dir}: {e}")
            except Exception as e:
                self.logger.error(f"Error scanning {templates_dir}: {e}")
        
        return frameworks
    
    def validate_mapping_files(self, frameworks: List[FrameworkInfo]) -> ValidationResult:
        """
        Validate that all frameworks have correctly named mapping files.
        
        Args:
            frameworks: List of FrameworkInfo objects to validate
            
        Returns:
            ValidationResult with validation status and details
        """
        valid_frameworks = []
        invalid_frameworks = []
        missing_files = []
        
        for framework in frameworks:
            if framework.has_mapping_file:
                valid_frameworks.append(framework)
            else:
                if framework.mapping_file_name:
                    # Has a mapping file but incorrectly named
                    invalid_frameworks.append(framework)
                else:
                    # No mapping file at all
                    missing_files.append(framework)
        
        total = len(frameworks)
        valid_count = len(valid_frameworks)
        success = (valid_count == total)
        
        return ValidationResult(
            total_frameworks=total,
            valid_frameworks=valid_count,
            invalid_frameworks=invalid_frameworks,
            missing_files=missing_files,
            success=success
        )
    
    def validate(self) -> ValidationResult:
        """
        Execute the complete validation process.
        
        Returns:
            ValidationResult with validation status and details
        """
        try:
            frameworks = self.scan_frameworks()
            result = self.validate_mapping_files(frameworks)
            return result
        except Exception as e:
            self.logger.error(f"Validation failed: {e}")
            return ValidationResult(
                total_frameworks=0,
                valid_frameworks=0,
                invalid_frameworks=[],
                missing_files=[],
                success=False,
                error=str(e)
            )
    
    def generate_report(self, result: ValidationResult) -> str:
        """
        Generate a human-readable report from validation results.
        
        Args:
            result: ValidationResult object
            
        Returns:
            Formatted report as a string
        """
        lines = []
        lines.append("=" * 80)
        lines.append("Framework Mapping File Validation Report")
        lines.append("=" * 80)
        lines.append("")
        
        if result.error:
            lines.append(f"ERROR: {result.error}")
            lines.append("")
            return "\n".join(lines)
        
        # Summary statistics
        lines.append("Summary:")
        lines.append(f"  Total Frameworks: {result.total_frameworks}")
        lines.append(f"  Valid Frameworks: {result.valid_frameworks}")
        lines.append(f"  Invalid Frameworks: {len(result.invalid_frameworks)}")
        lines.append(f"  Missing Files: {len(result.missing_files)}")
        lines.append(f"  Status: {'PASS' if result.success else 'FAIL'}")
        lines.append("")
        
        # List invalid frameworks (incorrectly named files)
        if result.invalid_frameworks:
            lines.append("Frameworks with Incorrectly Named Mapping Files:")
            for framework in result.invalid_frameworks:
                lines.append(f"  - {framework.language}/{framework.name}")
                lines.append(f"    Found: {framework.mapping_file_name}")
                lines.append(f"    Expected: {self.EXPECTED_MAPPING_FILE}")
            lines.append("")
        
        # List frameworks with missing files
        if result.missing_files:
            lines.append("Frameworks with Missing Mapping Files:")
            for framework in result.missing_files:
                lines.append(f"  - {framework.language}/{framework.name}")
                lines.append(f"    Path: {framework.path}")
            lines.append("")
        
        # Success message
        if result.success:
            lines.append("All frameworks have correctly named mapping files!")
        else:
            lines.append("Action Required: Fix the issues listed above.")
        
        lines.append("=" * 80)
        
        return "\n".join(lines)
