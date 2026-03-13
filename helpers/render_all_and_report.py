#!/usr/bin/env python3
"""
Render All Handbooks and Generate Report

This script renders all handbooks in markdown format and then generates
a comprehensive template list report comparing raw vs rendered versions.

Usage:
    python helpers/render_all_and_report.py [--languages LANG] [--output FILE]
"""

import argparse
import subprocess
import sys
from pathlib import Path
from typing import List, Tuple


# Mapping of handbook directory names
HANDBOOKS = [
    'bcm',
    'bsi-grundschutz',
    'cis-controls',
    'common-criteria',
    'coso',
    'csa-ccm',
    'dora',
    'gdpr',
    'hipaa',
    'idw-ps-951',
    'isms',
    'iso-31000',
    'iso-38500',
    'iso-9001',
    'it-operation',
    'nist-800-53',
    'nist-csf',
    'pci-dss',
    'soc1',
    'tisax',
    'togaf',
    'tsc'
]


def render_handbook(language: str, handbook: str, project_root: Path) -> bool:
    """
    Render a single handbook using the CLI.
    
    Args:
        language: Language code (de or en)
        handbook: Handbook name
        project_root: Project root directory
    
    Returns:
        True if successful, False otherwise
    """
    print(f"  Rendering {language}/{handbook}...", end=' ', flush=True)
    
    try:
        cmd = [
            sys.executable, '-m', 'src.cli',
            '--language', language,
            '--template', handbook,
            '--output', 'markdown',
            '--separate-files',
            '--test'
        ]
        
        result = subprocess.run(
            cmd,
            cwd=project_root,
            capture_output=True,
            text=True,
            timeout=300
        )
        
        if result.returncode == 0:
            print("✓")
            return True
        else:
            print(f"✗ (Error: {result.stderr[:100]})")
            return False
            
    except subprocess.TimeoutExpired:
        print("✗ (Timeout)")
        return False
    except Exception as e:
        print(f"✗ (Exception: {str(e)[:100]})")
        return False


def render_all_handbooks(languages: List[str], project_root: Path) -> Tuple[int, int]:
    """
    Render all handbooks for specified languages.
    
    Args:
        languages: List of language codes
        project_root: Project root directory
    
    Returns:
        Tuple of (successful_count, total_count)
    """
    total = 0
    successful = 0
    
    for language in languages:
        print(f"\n{'=' * 80}")
        print(f"Rendering {language.upper()} handbooks")
        print(f"{'=' * 80}")
        
        for handbook in HANDBOOKS:
            total += 1
            if render_handbook(language, handbook, project_root):
                successful += 1
    
    return successful, total


def generate_report(languages: List[str], output_file: str, project_root: Path) -> bool:
    """
    Generate template list report for all handbooks.
    
    Args:
        languages: List of language codes
        output_file: Output file path
        project_root: Project root directory
    
    Returns:
        True if successful, False otherwise
    """
    print(f"\n{'=' * 80}")
    print("Generating Template List Report")
    print(f"{'=' * 80}\n")
    
    try:
        # Build language filter
        if len(languages) == 1:
            lang_filter = languages[0]
        else:
            lang_filter = 'all'
        
        cmd = [
            sys.executable,
            'helpers/generate_template_list.py',
            '--source', 'both',
            '--language', lang_filter,
            '--output', output_file
        ]
        
        result = subprocess.run(
            cmd,
            cwd=project_root,
            capture_output=True,
            text=True,
            timeout=300
        )
        
        if result.returncode == 0:
            print(result.stdout)
            return True
        else:
            print(f"Error generating report: {result.stderr}")
            return False
            
    except Exception as e:
        print(f"Failed to generate report: {e}")
        return False


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Render all handbooks and generate comprehensive template list report',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Render all handbooks in both languages and generate report
  python helpers/render_all_and_report.py
  
  # Render only German handbooks
  python helpers/render_all_and_report.py --languages de
  
  # Render both languages with custom output file
  python helpers/render_all_and_report.py --languages de en --output my_report.txt
        """
    )
    
    parser.add_argument(
        '--languages',
        nargs='+',
        choices=['de', 'en'],
        default=['de', 'en'],
        help='Languages to render (default: de en)'
    )
    
    parser.add_argument(
        '--output',
        '-o',
        default='test-output/all_handbooks_report.txt',
        help='Output file path (default: test-output/all_handbooks_report.txt)'
    )
    
    args = parser.parse_args()
    
    # Determine project root
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    
    print("=" * 80)
    print("RENDER ALL HANDBOOKS AND GENERATE REPORT")
    print("=" * 80)
    print(f"Languages: {', '.join(args.languages)}")
    print(f"Handbooks: {len(HANDBOOKS)}")
    print(f"Total renders: {len(HANDBOOKS) * len(args.languages)}")
    print("=" * 80)
    
    # Step 1: Render all handbooks
    successful, total = render_all_handbooks(args.languages, project_root)
    
    print(f"\n{'=' * 80}")
    print("Rendering Summary")
    print(f"{'=' * 80}")
    print(f"Successful: {successful}/{total}")
    print(f"Failed: {total - successful}/{total}")
    
    if successful == 0:
        print("\nNo handbooks were rendered successfully. Aborting report generation.")
        return 1
    
    # Step 2: Generate template list report
    if generate_report(args.languages, args.output, project_root):
        print(f"\n{'=' * 80}")
        print("SUCCESS!")
        print(f"{'=' * 80}")
        print(f"All handbooks rendered and report generated.")
        print(f"Report saved to: {args.output}")
        print(f"JSON data saved to: {Path(args.output).with_suffix('.json')}")
        return 0
    else:
        print("\nReport generation failed.")
        return 1


if __name__ == '__main__':
    exit(main())
