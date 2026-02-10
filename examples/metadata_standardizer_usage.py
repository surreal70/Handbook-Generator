#!/usr/bin/env python3
"""
Example usage of MetadataStandardizer tool.

This script demonstrates how to use the MetadataStandardizer to:
1. Scan frameworks and detect missing metadata
2. Generate a standardization report
3. Enhance existing metadata files
4. Create new metadata files
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.metadata_standardizer import MetadataStandardizer


def main():
    # Initialize the standardizer
    standardizer = MetadataStandardizer('templates')
    
    print("Metadata Standardizer - Usage Example")
    print("=" * 60)
    
    # 1. Generate a report
    print("\n1. Generating standardization report...")
    report = standardizer.generate_report()
    print(f"\nSummary:")
    print(f"  Total frameworks: {report.total_frameworks}")
    print(f"  Complete frameworks: {report.frameworks_processed}")
    print(f"  Missing metadata files: {report.files_created}")
    print(f"  Files needing enhancement: {report.files_enhanced}")
    
    # 2. Detect missing metadata
    print("\n2. Detecting missing metadata files...")
    missing = standardizer.detect_missing_metadata()
    if missing:
        print(f"   Found {len(missing)} missing files:")
        for m in missing[:3]:
            print(f"     - {m.framework} ({m.language}): {m.expected_path}")
    
    # 3. Scan frameworks
    print("\n3. Scanning framework status...")
    status = standardizer.scan_frameworks()
    incomplete = [name for name, s in status.items() 
                  if not (s.de_metadata_complete and s.en_metadata_complete)]
    print(f"   {len(incomplete)} frameworks need attention:")
    for fw in incomplete[:5]:
        print(f"     - {fw}")
    
    # 4. Example: Validate a specific file
    print("\n4. Validating specific metadata file...")
    gdpr_path = Path('templates/de/gdpr/0000_metadata_de_gdpr.md')
    if gdpr_path.exists():
        result = standardizer.validate_metadata_structure(str(gdpr_path))
        print(f"   GDPR DE: {'✓ Valid' if result.is_valid else '✗ Invalid'}")
        if result.missing_fields:
            print(f"   Missing: {', '.join(result.missing_fields)}")
    
    print("\n" + "=" * 60)
    print("Example completed!")
    print("\nTo enhance metadata files, use:")
    print("  standardizer.enhance_existing_metadata('path/to/metadata.md')")
    print("\nTo create new metadata files, use:")
    print("  standardizer.create_metadata_file('framework-name', 'de')")


if __name__ == "__main__":
    main()
