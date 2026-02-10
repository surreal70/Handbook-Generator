#!/usr/bin/env python3
"""
Generate sample handbooks for all 7 new frameworks in all formats.

This script generates HTML, PDF, and Markdown handbooks for:
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
import subprocess
from pathlib import Path


def main():
    """Generate sample handbooks for all frameworks."""
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
    
    print("=" * 80)
    print("SAMPLE HANDBOOK GENERATION")
    print("=" * 80)
    print()
    print(f"Generating handbooks for {len(frameworks)} frameworks in {len(languages)} languages")
    print(f"Total: {len(frameworks) * len(languages)} handbooks")
    print()
    
    success_count = 0
    failure_count = 0
    
    for framework in frameworks:
        for language in languages:
            print(f"Generating {framework} ({language})...")
            
            # Generate HTML handbook
            cmd = [
                './handbook-generator',
                '-l', language,
                '-t', framework,
                '-o', 'html',
                '--test'
            ]
            
            try:
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
                if result.returncode == 0:
                    print(f"  ✓ HTML generated successfully")
                    success_count += 1
                else:
                    print(f"  ✗ HTML generation failed: {result.stderr[:100]}")
                    failure_count += 1
            except Exception as e:
                print(f"  ✗ HTML generation error: {str(e)[:100]}")
                failure_count += 1
            
            # Generate Markdown handbook
            cmd = [
                './handbook-generator',
                '-l', language,
                '-t', framework,
                '-o', 'markdown',
                '--test',
                '--separate-files'
            ]
            
            try:
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
                if result.returncode == 0:
                    print(f"  ✓ Markdown generated successfully")
                    success_count += 1
                else:
                    print(f"  ✗ Markdown generation failed: {result.stderr[:100]}")
                    failure_count += 1
            except Exception as e:
                print(f"  ✗ Markdown generation error: {str(e)[:100]}")
                failure_count += 1
            
            print()
    
    # Summary
    print("=" * 80)
    print("GENERATION SUMMARY")
    print("=" * 80)
    print()
    print(f"Successful: {success_count}")
    print(f"Failed: {failure_count}")
    print(f"Total: {success_count + failure_count}")
    print()
    
    if failure_count == 0:
        print("✓ ALL HANDBOOKS GENERATED SUCCESSFULLY")
        return 0
    else:
        print(f"✗ {failure_count} HANDBOOKS FAILED TO GENERATE")
        return 1


if __name__ == '__main__':
    sys.exit(main())
