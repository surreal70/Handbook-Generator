#!/usr/bin/env python3
"""
Enhance existing metadata files by adding missing fields.

This script enhances existing metadata files with missing required fields,
including template_version and revision.
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent.parent / 'src'))

from metadata_standardizer import MetadataStandardizer


def main():
    """Enhance existing metadata files."""
    # Parse command line arguments
    if len(sys.argv) > 1:
        frameworks_to_enhance = sys.argv[1:]
    else:
        # Default: enhance all frameworks
        frameworks_to_enhance = None
    
    print("=" * 70)
    print("ENHANCE EXISTING METADATA FILES")
    print("=" * 70)
    print()
    
    # Initialize standardizer
    templates_dir = Path(__file__).parent.parent / 'templates'
    standardizer = MetadataStandardizer(str(templates_dir))
    
    # Get framework status
    frameworks_status = standardizer.scan_frameworks()
    
    # Filter frameworks if specified
    if frameworks_to_enhance:
        frameworks_status = {
            name: status for name, status in frameworks_status.items()
            if name in frameworks_to_enhance
        }
    
    # Enhance frameworks that need it
    enhanced_count = 0
    failed_count = 0
    skipped_count = 0
    
    for framework, status in sorted(frameworks_status.items()):
        print(f"\nProcessing {framework}...")
        
        # Enhance DE metadata if needed
        if status.has_de_metadata:
            if not status.de_metadata_complete:
                de_path = standardizer._get_metadata_path(framework, 'de')
                print(f"  Enhancing DE metadata...")
                print(f"    Missing fields: {', '.join(status.missing_fields)}")
                try:
                    success = standardizer.enhance_existing_metadata(str(de_path))
                    if success:
                        print(f"    ✓ Enhanced: {de_path}")
                        enhanced_count += 1
                    else:
                        print(f"    ✗ Failed to enhance: {de_path}")
                        failed_count += 1
                except Exception as e:
                    print(f"    ✗ Error: {e}")
                    failed_count += 1
            else:
                print(f"  ✓ DE metadata already complete")
                skipped_count += 1
        
        # Enhance EN metadata if needed
        if status.has_en_metadata:
            if not status.en_metadata_complete:
                en_path = standardizer._get_metadata_path(framework, 'en')
                print(f"  Enhancing EN metadata...")
                print(f"    Missing fields: {', '.join(status.missing_fields)}")
                try:
                    success = standardizer.enhance_existing_metadata(str(en_path))
                    if success:
                        print(f"    ✓ Enhanced: {en_path}")
                        enhanced_count += 1
                    else:
                        print(f"    ✗ Failed to enhance: {en_path}")
                        failed_count += 1
                except Exception as e:
                    print(f"    ✗ Error: {e}")
                    failed_count += 1
            else:
                print(f"  ✓ EN metadata already complete")
                skipped_count += 1
    
    print()
    print("=" * 70)
    print("ENHANCEMENT COMPLETE")
    print("=" * 70)
    print(f"  Enhanced: {enhanced_count}")
    print(f"  Skipped (already complete): {skipped_count}")
    print(f"  Failed: {failed_count}")
    print()
    
    return 0 if failed_count == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
