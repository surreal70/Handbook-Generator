#!/usr/bin/env python3
"""
Validate all compliance frameworks in German and English.

This script validates all 7 new frameworks:
- cis-controls
- common-criteria
- gdpr
- hipaa
- iso-9001
- nist-800-53
- pci-dss
- tsc

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright (c) 2026
"""

import sys
from pathlib import Path
from src.template_validator import TemplateValidator


def main():
    """Validate all frameworks in both languages."""
    frameworks = [
        'cis-controls',
        'common-criteria',
        'gdpr',
        'hipaa',
        'iso-9001',
        'nist-800-53',
        'pci-dss',
        'tsc'
    ]
    
    languages = ['de', 'en']
    templates_dir = Path('templates')
    
    validator = TemplateValidator()
    all_valid = True
    results = {}
    
    print("=" * 80)
    print("FRAMEWORK VALIDATION REPORT")
    print("=" * 80)
    print()
    
    for framework in frameworks:
        results[framework] = {}
        
        for language in languages:
            print(f"Validating {framework} ({language})...")
            result = validator.validate_framework(language, framework, templates_dir)
            results[framework][language] = result
            
            if result.is_valid:
                print(f"  ✓ VALID")
            else:
                print(f"  ✗ INVALID")
                all_valid = False
            
            if result.errors:
                print(f"  Errors: {len(result.errors)}")
                for error in result.errors:
                    print(f"    - {error}")
            
            if result.warnings:
                print(f"  Warnings: {len(result.warnings)}")
                for warning in result.warnings:
                    print(f"    - {warning}")
            
            print()
    
    # Summary
    print("=" * 80)
    print("VALIDATION SUMMARY")
    print("=" * 80)
    print()
    
    for framework in frameworks:
        de_result = results[framework]['de']
        en_result = results[framework]['en']
        
        de_status = "✓" if de_result.is_valid else "✗"
        en_status = "✓" if en_result.is_valid else "✗"
        
        print(f"{framework:20s} DE: {de_status}  EN: {en_status}")
    
    print()
    print("=" * 80)
    
    if all_valid:
        print("✓ ALL FRAMEWORKS VALID")
        return 0
    else:
        print("✗ SOME FRAMEWORKS HAVE ERRORS")
        return 1


if __name__ == '__main__':
    sys.exit(main())
