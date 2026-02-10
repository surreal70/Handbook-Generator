#!/usr/bin/env python3
"""
Example script demonstrating framework validation.

This script shows how to use the extended validation system to validate
compliance framework templates.

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright (c) 2026
"""

from pathlib import Path
from src.template_validator import TemplateValidator


def main():
    """Validate all compliance frameworks."""
    validator = TemplateValidator()
    
    # List of frameworks to validate
    frameworks = [
        'pci-dss',
        'hipaa',
        'nist-800-53',
        'tsc',
        'common-criteria',
        'iso-9001',
        'gdpr'
    ]
    
    print("=" * 80)
    print("Framework Validation Report")
    print("=" * 80)
    
    for framework in frameworks:
        print(f"\n{'=' * 80}")
        print(f"Framework: {framework.upper()}")
        print(f"{'=' * 80}")
        
        # Validate German templates
        result = validator.validate_framework('de', framework)
        
        print(f"\nValidation Status: {'✓ PASSED' if result.is_valid else '✗ FAILED'}")
        print(f"Errors: {len(result.errors)}")
        print(f"Warnings: {len(result.warnings)}")
        
        if result.errors:
            print("\nErrors:")
            for error in result.errors:
                print(f"  • {error}")
        
        if result.warnings:
            print(f"\nWarnings (showing first 5 of {len(result.warnings)}):")
            for warning in result.warnings[:5]:
                print(f"  • {warning}")
    
    print(f"\n{'=' * 80}")
    print("Validation Complete")
    print(f"{'=' * 80}")


if __name__ == '__main__':
    main()
