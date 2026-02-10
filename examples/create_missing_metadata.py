#!/usr/bin/env python3
"""
Create missing metadata files for frameworks.

This script creates metadata files for frameworks that are missing them,
using the unified structure with all required fields.
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from metadata_standardizer import MetadataStandardizer


def main():
    """Create missing metadata files."""
    print("=" * 70)
    print("CREATE MISSING METADATA FILES")
    print("=" * 70)
    print()
    
    # Initialize standardizer
    templates_dir = Path(__file__).parent.parent / 'templates'
    standardizer = MetadataStandardizer(str(templates_dir))
    
    # Detect missing metadata
    missing = standardizer.detect_missing_metadata()
    
    if not missing:
        print("No missing metadata files found!")
        return 0
    
    print(f"Found {len(missing)} missing metadata files:")
    for item in missing:
        print(f"  - {item.framework} ({item.language})")
    print()
    
    # Create missing files
    created_count = 0
    failed_count = 0
    
    for item in missing:
        print(f"Creating metadata for {item.framework} ({item.language})...")
        try:
            success = standardizer.create_metadata_file(item.framework, item.language)
            if success:
                print(f"  ✓ Created: {item.expected_path}")
                created_count += 1
            else:
                print(f"  ✗ Failed to create: {item.expected_path}")
                failed_count += 1
        except FileExistsError:
            print(f"  ⚠ Already exists: {item.expected_path}")
        except Exception as e:
            print(f"  ✗ Error: {e}")
            failed_count += 1
    
    print()
    print("=" * 70)
    print("CREATION COMPLETE")
    print("=" * 70)
    print(f"  Created: {created_count}")
    print(f"  Failed: {failed_count}")
    print()
    
    return 0 if failed_count == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
