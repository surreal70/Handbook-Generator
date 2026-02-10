#!/usr/bin/env python3
"""
Scan and analyze existing metadata across all frameworks.

This script runs the metadata standardizer scan and generates a detailed
report of the current state of metadata files.
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from metadata_standardizer import MetadataStandardizer


def main():
    """Run metadata scan and generate report."""
    print("=" * 70)
    print("METADATA STANDARDIZATION SCAN")
    print("=" * 70)
    print()
    
    # Initialize standardizer
    templates_dir = Path(__file__).parent.parent / 'templates'
    standardizer = MetadataStandardizer(str(templates_dir))
    
    # Generate report
    report = standardizer.generate_report()
    
    # Print report
    print(report.summary)
    print()
    
    # Print missing metadata files
    print()
    print("=" * 70)
    print("MISSING METADATA FILES")
    print("=" * 70)
    missing = standardizer.detect_missing_metadata()
    
    if missing:
        for item in missing:
            print(f"  {item.framework:25} ({item.language}): {item.expected_path}")
    else:
        print("  No missing metadata files found!")
    
    print()
    print("=" * 70)
    print("SCAN COMPLETE")
    print("=" * 70)
    print()
    print(f"Summary:")
    print(f"  - Total frameworks: {report.total_frameworks}")
    print(f"  - Complete metadata: {report.frameworks_processed}")
    print(f"  - Missing files: {report.files_created}")
    print(f"  - Files needing enhancement: {report.files_enhanced}")
    print(f"  - Validation errors: {report.validation_errors}")
    print()
    
    # Return exit code based on results
    if report.validation_errors > 0 or report.files_created > 0 or report.files_enhanced > 0:
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
