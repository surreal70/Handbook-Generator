#!/usr/bin/env python3
"""
Generate a placeholder coverage matrix for all handbooks.

This script analyzes:
- All placeholders used in handbook templates
- All placeholders defined in config files
- Coverage status for each handbook

Exclusions:
- README files are excluded from analysis (they contain placeholder examples for documentation)

Output Matrix:
- X-axis: All unique placeholders
- Y-axis: All handbooks
- Symbols:
  # (green)  - Placeholder is used in the handbook
  O (blue)   - Placeholder is defined but not used in the handbook
  X (red)    - Placeholder is used but not defined in any config file

Usage:
  python generate_placeholder_matrix.py                    # Analyze all handbooks
  python generate_placeholder_matrix.py --handbook isms    # Analyze specific handbook
  python generate_placeholder_matrix.py --language de      # Analyze specific language
  python generate_placeholder_matrix.py --handbook isms --language de  # Specific handbook and language
"""

import re
import yaml
import argparse
from pathlib import Path
from collections import defaultdict
from typing import Dict, Set, List, Tuple, Optional


# ANSI color codes
class Colors:
    GREEN = '\033[92m'
    BLUE = '\033[94m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    RESET = '\033[0m'
    BOLD = '\033[1m'


def extract_placeholders_from_file(filepath: Path) -> Set[str]:
    """Extract all placeholders from a markdown file."""
    placeholders = set()
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Match {{ placeholder }} pattern (including hyphens and dots like meta-handbook.field)
        # Pattern supports: letters, numbers, underscores, hyphens, and dots
        # Also handles optional spaces around the placeholder
        matches = re.findall(r'\{\{\s*([a-zA-Z0-9_\.\-]+)\s*\}\}', content)
        placeholders.update(matches)
        
    except Exception as e:
        print(f"Warning: Could not read {filepath}: {e}")
    
    return placeholders


def extract_placeholders_with_locations(filepath: Path) -> Dict[str, List[int]]:
    """Extract all placeholders from a markdown file with their line numbers."""
    placeholder_locations = defaultdict(list)
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            lines = f.readlines()
        
        for line_num, line in enumerate(lines, start=1):
            # Match {{ placeholder }} pattern
            matches = re.findall(r'\{\{\s*([a-zA-Z0-9_\.\-]+)\s*\}\}', line)
            for match in matches:
                placeholder_locations[match].append(line_num)
        
    except Exception as e:
        print(f"Warning: Could not read {filepath}: {e}")
    
    return dict(placeholder_locations)


def load_config_placeholders() -> Dict[str, Set[str]]:
    """Load all placeholders defined in config files."""
    config_placeholders = {}
    
    config_files = {
        'meta-global.yaml': 'meta-global',
        'meta-organisation.yaml': 'meta-organisation',
        'meta-organisation-roles.yaml': 'meta-organisation-roles',
    }
    
    for config_file, prefix in config_files.items():
        config_path = Path(config_file)
        if not config_path.exists():
            print(f"Warning: Config file not found: {config_file}")
            continue
        
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
            
            if data:
                # Prefix placeholders with their namespace to match template usage
                placeholders = set(f"{prefix}.{key}" for key in data.keys())
                config_placeholders[config_file] = placeholders
        except Exception as e:
            print(f"Warning: Could not load {config_file}: {e}")
    
    return config_placeholders


def load_handbook_specific_placeholders() -> Dict[str, Set[str]]:
    """Load placeholders from handbook-specific meta files."""
    handbook_placeholders = {}
    templates_dir = Path('templates')
    
    for lang_dir in ['de', 'en']:
        lang_path = templates_dir / lang_dir
        if not lang_path.exists():
            continue
        
        for handbook_dir in lang_path.iterdir():
            if not handbook_dir.is_dir():
                continue
            
            meta_file = handbook_dir / 'meta-handbook.yaml'
            if not meta_file.exists():
                continue
            
            try:
                with open(meta_file, 'r', encoding='utf-8') as f:
                    data = yaml.safe_load(f)
                
                if data:
                    handbook_key = f"{lang_dir}/{handbook_dir.name}"
                    # Prefix placeholders with meta-handbook. to match template usage
                    placeholders = set(f"meta-handbook.{key}" for key in data.keys())
                    
                    # Also check for auxiliary placeholders
                    if 'auxiliary' in data and isinstance(data['auxiliary'], dict):
                        aux_placeholders = set(f"meta-handbook.{key}" for key in data['auxiliary'].keys())
                        placeholders.update(aux_placeholders)
                    
                    handbook_placeholders[handbook_key] = placeholders
            except Exception as e:
                print(f"Warning: Could not load {meta_file}: {e}")
    
    return handbook_placeholders


def analyze_handbooks(handbook_filter: Optional[str] = None, 
                     language_filter: Optional[str] = None) -> Tuple[Dict[str, Set[str]], Set[str], Dict[str, List[Tuple[str, int]]]]:
    """
    Analyze all handbooks and extract placeholder usage.
    
    Args:
        handbook_filter: Optional handbook name to filter (e.g., 'isms', 'it-operation')
        language_filter: Optional language to filter ('de' or 'en')
    
    Returns:
        Tuple of (handbook_placeholders, all_defined_placeholders, undefined_locations)
        where undefined_locations maps placeholder -> [(file, line_num), ...]
    """
    templates_dir = Path('templates')
    handbook_usage = {}
    undefined_locations = defaultdict(list)
    
    # Load all defined placeholders from config files
    config_placeholders = load_config_placeholders()
    handbook_specific = load_handbook_specific_placeholders()
    
    # Combine all defined placeholders
    all_defined = set()
    for placeholders in config_placeholders.values():
        all_defined.update(placeholders)
    for placeholders in handbook_specific.values():
        all_defined.update(placeholders)
    
    # Determine which languages to analyze
    languages = [language_filter] if language_filter else ['de', 'en']
    
    # Analyze each handbook
    for lang_dir in languages:
        lang_path = templates_dir / lang_dir
        if not lang_path.exists():
            continue
        
        for handbook_dir in sorted(lang_path.iterdir()):
            if not handbook_dir.is_dir():
                continue
            
            # Apply handbook filter if specified
            if handbook_filter and handbook_dir.name != handbook_filter:
                continue
            
            handbook_key = f"{lang_dir}/{handbook_dir.name}"
            used_placeholders = set()
            
            # Scan all markdown files in the handbook (excluding README files)
            for md_file in handbook_dir.glob('*.md'):
                # Skip README files - they contain placeholder examples for documentation
                if md_file.name.upper().startswith('README'):
                    continue
                
                placeholders = extract_placeholders_from_file(md_file)
                used_placeholders.update(placeholders)
                
                # Track locations of undefined placeholders
                placeholder_locs = extract_placeholders_with_locations(md_file)
                for placeholder, line_nums in placeholder_locs.items():
                    if placeholder not in all_defined:
                        # Store relative path from templates dir
                        rel_path = md_file.relative_to(templates_dir)
                        for line_num in line_nums:
                            undefined_locations[placeholder].append((str(rel_path), line_num))
            
            handbook_usage[handbook_key] = used_placeholders
    
    return handbook_usage, all_defined, dict(undefined_locations)


def generate_matrix(handbook_usage: Dict[str, Set[str]], 
                    all_defined: Set[str]) -> None:
    """Generate and display the placeholder coverage matrix."""
    
    # Get all unique placeholders (used or defined)
    all_placeholders = set()
    for placeholders in handbook_usage.values():
        all_placeholders.update(placeholders)
    all_placeholders.update(all_defined)
    
    # Sort for consistent output
    sorted_placeholders = sorted(all_placeholders)
    sorted_handbooks = sorted(handbook_usage.keys())
    
    # Calculate statistics
    stats = {
        'total_placeholders': len(sorted_placeholders),
        'total_handbooks': len(sorted_handbooks),
        'used_count': 0,
        'defined_unused_count': 0,
        'undefined_count': 0,
    }
    
    # Calculate unique placeholder counts
    all_used = set()
    for used in handbook_usage.values():
        all_used.update(used)
    
    unique_stats = {
        'used_and_defined': len([ph for ph in all_used if ph in all_defined]),
        'used_but_undefined': len([ph for ph in all_used if ph not in all_defined]),
        'defined_but_unused': len(all_defined - all_used),
    }
    
    # Print header
    print(f"\n{Colors.BOLD}Placeholder Coverage Matrix{Colors.RESET}")
    print("=" * 80)
    print(f"Total Unique Placeholders: {len(sorted_placeholders)}")
    print(f"Total Handbooks: {len(sorted_handbooks)}")
    print(f"\nUnique Placeholder Status:")
    print(f"  {Colors.GREEN}Used & Defined:{Colors.RESET} {unique_stats['used_and_defined']}")
    print(f"  {Colors.BLUE}Defined but Unused:{Colors.RESET} {unique_stats['defined_but_unused']}")
    print(f"  {Colors.RED}Used but Undefined:{Colors.RESET} {unique_stats['used_but_undefined']}")
    print(f"\nLegend:")
    print(f"  {Colors.GREEN}#{Colors.RESET} - Placeholder is used in handbook")
    print(f"  {Colors.BLUE}O{Colors.RESET} - Placeholder is defined but not used")
    print(f"  {Colors.RED}X{Colors.RESET} - Placeholder is used but not defined in config")
    print("=" * 80)
    
    # Print matrix header (placeholders as columns)
    # Due to space constraints, we'll print in sections
    col_width = 3
    max_cols_per_section = 25
    
    for section_start in range(0, len(sorted_handbooks), max_cols_per_section):
        section_end = min(section_start + max_cols_per_section, len(sorted_handbooks))
        section_handbooks = sorted_handbooks[section_start:section_end]
        
        print(f"\n{Colors.YELLOW}Section: Handbooks {section_start + 1}-{section_end}{Colors.RESET}")
        print("-" * 80)
        
        # Print handbook names (abbreviated)
        print(f"{'Placeholder':<40}", end='')
        for hb in section_handbooks:
            # Abbreviate handbook name
            abbrev = hb[:col_width-1] if len(hb) > col_width-1 else hb
            print(f"{abbrev:>{col_width}}", end='')
        print()
        
        print("-" * 80)
        
        # Print each placeholder row
        for placeholder in sorted_placeholders:
            # Abbreviate placeholder name for display
            ph_display = placeholder[:38] if len(placeholder) > 38 else placeholder
            print(f"{ph_display:<40}", end='')
            
            for handbook in section_handbooks:
                used = handbook_usage[handbook]
                
                if placeholder in used:
                    if placeholder in all_defined:
                        # Used and defined
                        symbol = f"{Colors.GREEN}#{Colors.RESET}"
                        stats['used_count'] += 1
                    else:
                        # Used but not defined
                        symbol = f"{Colors.RED}X{Colors.RESET}"
                        stats['undefined_count'] += 1
                elif placeholder in all_defined:
                    # Defined but not used
                    symbol = f"{Colors.BLUE}O{Colors.RESET}"
                    stats['defined_unused_count'] += 1
                else:
                    # Neither used nor defined (shouldn't happen)
                    symbol = " "
                
                print(f"{symbol:>{col_width}}", end='')
            print()
    
    # Print full placeholder list
    print(f"\n{Colors.BOLD}Full Placeholder List:{Colors.RESET}")
    print("-" * 80)
    for i, ph in enumerate(sorted_placeholders, 1):
        status = "defined" if ph in all_defined else "undefined"
        color = Colors.GREEN if ph in all_defined else Colors.RED
        print(f"{i:3d}. {color}{ph:<40}{Colors.RESET} [{status}]")
    
    # Print summary statistics
    print(f"\n{Colors.BOLD}Summary Statistics:{Colors.RESET}")
    print("=" * 80)
    print(f"Total Unique Placeholders: {stats['total_placeholders']}")
    print(f"Total Handbooks: {stats['total_handbooks']}")
    print(f"\n{Colors.BOLD}Unique Placeholder Status:{Colors.RESET}")
    print(f"{Colors.GREEN}Used & Defined:{Colors.RESET} {unique_stats['used_and_defined']} unique placeholders")
    print(f"{Colors.BLUE}Defined but Unused:{Colors.RESET} {unique_stats['defined_but_unused']} unique placeholders")
    print(f"{Colors.RED}Used but Undefined:{Colors.RESET} {unique_stats['used_but_undefined']} unique placeholders")
    print(f"\n{Colors.BOLD}Matrix Cell Counts (Placeholder × Handbook):{Colors.RESET}")
    print(f"{Colors.GREEN}Used & Defined:{Colors.RESET} {stats['used_count']} cells")
    print(f"{Colors.BLUE}Defined but Unused:{Colors.RESET} {stats['defined_unused_count']} cells")
    print(f"{Colors.RED}Used but Undefined:{Colors.RESET} {stats['undefined_count']} cells")
    
    # Find undefined placeholders
    undefined = set()
    for handbook, used in handbook_usage.items():
        for ph in used:
            if ph not in all_defined:
                undefined.add(ph)
    
    # Find unused placeholders
    all_used = set()
    for used in handbook_usage.values():
        all_used.update(used)
    unused = sorted(all_defined - all_used)
    
    if undefined:
        print(f"\n{Colors.RED}{Colors.BOLD}Undefined Placeholders:{Colors.RESET}")
        for ph in sorted(undefined):
            print(f"  - {ph}")
    
    if unused:
        print(f"\n{Colors.BLUE}{Colors.BOLD}Defined but Unused Placeholders ({len(unused)}):{Colors.RESET}")
        print(f"{Colors.BLUE}These placeholders are defined in config files but not used in any template:{Colors.RESET}")
        # Print in columns for better readability
        cols = 3
        for i in range(0, len(unused), cols):
            row = unused[i:i+cols]
            print("  " + "  ".join(f"{ph:<40}" for ph in row))


def generate_csv_report(handbook_usage: Dict[str, Set[str]], 
                       all_defined: Set[str],
                       output_file: str = 'placeholder_matrix.csv') -> None:
    """Generate a CSV report of the placeholder matrix."""
    
    all_placeholders = set()
    for placeholders in handbook_usage.values():
        all_placeholders.update(placeholders)
    all_placeholders.update(all_defined)
    
    sorted_placeholders = sorted(all_placeholders)
    sorted_handbooks = sorted(handbook_usage.keys())
    
    with open(output_file, 'w', encoding='utf-8') as f:
        # Write header (handbooks as columns)
        f.write('Placeholder,' + ','.join(sorted_handbooks) + '\n')
        
        # Write each placeholder row
        for placeholder in sorted_placeholders:
            row = [placeholder]
            
            for handbook in sorted_handbooks:
                used = handbook_usage[handbook]
                
                if placeholder in used:
                    if placeholder in all_defined:
                        symbol = '#'  # Used and defined
                    else:
                        symbol = 'X'  # Used but not defined
                elif placeholder in all_defined:
                    symbol = 'O'  # Defined but not used
                else:
                    symbol = ''
                
                row.append(symbol)
            
            f.write(','.join(row) + '\n')
    
    print(f"\n{Colors.GREEN}CSV report generated: {output_file}{Colors.RESET}")


def generate_html_report(handbook_usage: Dict[str, Set[str]], 
                        all_defined: Set[str],
                        undefined_locations: Dict[str, List[Tuple[str, int]]],
                        output_file: str = 'placeholder_matrix.html') -> None:
    """Generate an HTML report of the placeholder matrix."""
    
    all_placeholders = set()
    for placeholders in handbook_usage.values():
        all_placeholders.update(placeholders)
    all_placeholders.update(all_defined)
    
    sorted_placeholders = sorted(all_placeholders)
    sorted_handbooks = sorted(handbook_usage.keys())
    
    # Calculate cell-based statistics (for matrix visualization)
    cell_stats = {
        'total_placeholders': len(sorted_placeholders),
        'total_handbooks': len(sorted_handbooks),
        'used_count': 0,
        'defined_unused_count': 0,
        'undefined_count': 0,
    }
    
    # Count cell statistics
    for handbook, used in handbook_usage.items():
        for placeholder in sorted_placeholders:
            if placeholder in used:
                if placeholder in all_defined:
                    cell_stats['used_count'] += 1
                else:
                    cell_stats['undefined_count'] += 1
            elif placeholder in all_defined:
                cell_stats['defined_unused_count'] += 1
    
    # Calculate unique placeholder statistics
    all_used = set()
    for used in handbook_usage.values():
        all_used.update(used)
    
    unique_stats = {
        'used_and_defined': len([ph for ph in all_used if ph in all_defined]),
        'used_but_undefined': len([ph for ph in all_used if ph not in all_defined]),
        'defined_but_unused': len(all_defined - all_used),
    }
    
    # Find undefined placeholders
    undefined = set()
    for handbook, used in handbook_usage.items():
        for ph in used:
            if ph not in all_defined:
                undefined.add(ph)
    
    # Generate HTML
    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Placeholder Coverage Matrix</title>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 100%;
            background-color: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #333;
            border-bottom: 3px solid #4CAF50;
            padding-bottom: 10px;
        }}
        .stats {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 15px;
            margin: 20px 0;
        }}
        .stat-card {{
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            padding: 15px;
            border-radius: 8px;
            text-align: center;
        }}
        .stat-card h3 {{
            margin: 0;
            font-size: 2em;
        }}
        .stat-card p {{
            margin: 5px 0 0 0;
            opacity: 0.9;
        }}
        .legend {{
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
            border-left: 4px solid #4CAF50;
        }}
        .legend h2 {{
            margin-top: 0;
            color: #333;
        }}
        .legend-item {{
            display: inline-block;
            margin-right: 30px;
            margin-bottom: 10px;
        }}
        .legend-symbol {{
            display: inline-block;
            width: 30px;
            height: 30px;
            text-align: center;
            line-height: 30px;
            border-radius: 4px;
            font-weight: bold;
            margin-right: 8px;
        }}
        .symbol-used {{
            background-color: #4CAF50;
            color: white;
        }}
        .symbol-unused {{
            background-color: #2196F3;
            color: white;
        }}
        .symbol-undefined {{
            background-color: #f44336;
            color: white;
        }}
        .table-container {{
            overflow-x: auto;
            margin: 20px 0;
            border: 1px solid #ddd;
            border-radius: 8px;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            font-size: 12px;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: center;
        }}
        th {{
            background-color: #4CAF50;
            color: white;
            position: sticky;
            top: 0;
            z-index: 10;
            font-weight: bold;
        }}
        th.handbook-header {{
            background-color: #2196F3;
            text-align: left;
            min-width: 200px;
            position: sticky;
            left: 0;
            z-index: 11;
        }}
        td.handbook-name {{
            background-color: #f9f9f9;
            text-align: left;
            font-weight: bold;
            position: sticky;
            left: 0;
            z-index: 5;
        }}
        tr:hover td {{
            background-color: #fffde7;
        }}
        .cell-used {{
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
        }}
        .cell-unused {{
            background-color: #2196F3;
            color: white;
        }}
        .cell-undefined {{
            background-color: #f44336;
            color: white;
            font-weight: bold;
        }}
        .undefined-list {{
            background-color: #ffebee;
            padding: 15px;
            border-radius: 8px;
            margin: 20px 0;
            border-left: 4px solid #f44336;
        }}
        .undefined-list h2 {{
            margin-top: 0;
            color: #c62828;
        }}
        .undefined-list ul {{
            columns: 3;
            -webkit-columns: 3;
            -moz-columns: 3;
        }}
        .placeholder-header {{
            writing-mode: vertical-rl;
            transform: rotate(180deg);
            white-space: nowrap;
            max-width: 30px;
            font-size: 11px;
        }}
        @media print {{
            body {{
                background-color: white;
            }}
            .container {{
                box-shadow: none;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Placeholder Coverage Matrix</h1>
        
        <div class="stats">
            <div class="stat-card">
                <h3>{unique_stats['used_and_defined']}</h3>
                <p>Unique Placeholders Used</p>
            </div>
            <div class="stat-card">
                <h3>{unique_stats['defined_but_unused']}</h3>
                <p>Unique Placeholders Unused</p>
            </div>
            <div class="stat-card">
                <h3>{unique_stats['used_but_undefined']}</h3>
                <p>Unique Placeholders Undefined</p>
            </div>
            <div class="stat-card" style="background: linear-gradient(135deg, #9C27B0 0%, #673AB7 100%);">
                <h3>{cell_stats['total_placeholders']}</h3>
                <p>Total Unique Placeholders</p>
            </div>
            <div class="stat-card" style="background: linear-gradient(135deg, #FF9800 0%, #F57C00 100%);">
                <h3>{cell_stats['total_handbooks']}</h3>
                <p>Total Handbooks</p>
            </div>
        </div>
        
        <div style="background-color: #fff3e0; padding: 15px; border-radius: 8px; margin: 20px 0; border-left: 4px solid #FF9800;">
            <h3 style="margin-top: 0; color: #E65100;">📊 Matrix Statistics</h3>
            <p style="margin: 5px 0;">The matrix below shows {cell_stats['used_count']:,} cells where placeholders are used and defined, 
            {cell_stats['defined_unused_count']:,} cells where placeholders are defined but unused, 
            and {cell_stats['undefined_count']:,} cells where placeholders are used but undefined.</p>
            <p style="margin: 5px 0; font-size: 0.9em; color: #666;">
                <strong>Note:</strong> Cell counts represent placeholder × handbook combinations. 
                For example, if 1 placeholder is unused in 44 handbooks, that's 44 cells.
            </p>
        </div>
        
        <div class="legend">
            <h2>Legend</h2>
            <div class="legend-item">
                <span class="legend-symbol symbol-used">#</span>
                <span>Placeholder is used in handbook and defined in config</span>
            </div>
            <div class="legend-item">
                <span class="legend-symbol symbol-unused">O</span>
                <span>Placeholder is defined but not used in handbook</span>
            </div>
            <div class="legend-item">
                <span class="legend-symbol symbol-undefined">X</span>
                <span>Placeholder is used but NOT defined in config</span>
            </div>
        </div>
"""
    
    # Add the matrix table
    html += """
        <div class="table-container">
            <table>
                <thead>
                    <tr>
                        <th class="handbook-header">Placeholder</th>
"""
    
    # Add handbook headers
    for handbook in sorted_handbooks:
        html += f'                        <th><div class="placeholder-header">{handbook}</div></th>\n'
    
    html += """                    </tr>
                </thead>
                <tbody>
"""
    
    # Add placeholder rows
    for placeholder in sorted_placeholders:
        html += f'                    <tr>\n'
        html += f'                        <td class="handbook-name">{placeholder}</td>\n'
        
        for handbook in sorted_handbooks:
            used = handbook_usage[handbook]
            
            if placeholder in used:
                if placeholder in all_defined:
                    cell_class = 'cell-used'
                    symbol = '#'
                else:
                    cell_class = 'cell-undefined'
                    symbol = 'X'
            elif placeholder in all_defined:
                cell_class = 'cell-unused'
                symbol = 'O'
            else:
                cell_class = ''
                symbol = ''
            
            html += f'                        <td class="{cell_class}">{symbol}</td>\n'
        
        html += '                    </tr>\n'
    
    html += """                </tbody>
            </table>
        </div>
"""
    
    # Find unused placeholders (defined but never used)
    all_used = set()
    for used in handbook_usage.values():
        all_used.update(used)
    
    unused = sorted(all_defined - all_used)
    
    # Add undefined placeholders section at the end if any
    if undefined:
        html += f"""
        <div class="undefined-list" style="margin-top: 40px;">
            <h2>⚠️ Undefined Placeholders ({len(undefined)})</h2>
            <p>These placeholders are used in templates but not defined in any config file:</p>
"""
        for ph in sorted(undefined):
            html += f"""
            <div style="margin-bottom: 20px; padding: 10px; background-color: white; border-radius: 4px;">
                <h3 style="margin-top: 0; color: #d32f2f;"><code>{ph}</code></h3>
                <p style="margin: 5px 0; font-weight: bold;">Used in:</p>
                <ul style="margin: 5px 0; padding-left: 20px;">
"""
            if ph in undefined_locations:
                # Group by file
                locations_by_file = defaultdict(list)
                for file_path, line_num in undefined_locations[ph]:
                    locations_by_file[file_path].append(line_num)
                
                for file_path in sorted(locations_by_file.keys()):
                    line_nums = sorted(locations_by_file[file_path])
                    line_nums_str = ', '.join(f"line {ln}" for ln in line_nums)
                    html += f'                    <li><code>{file_path}</code> ({line_nums_str})</li>\n'
            else:
                html += '                    <li><em>No location information available</em></li>\n'
            
            html += """                </ul>
            </div>
"""
        html += """        </div>
"""
    
    # Add unused placeholders section
    if unused:
        html += f"""
        <div style="background-color: #e3f2fd; padding: 15px; border-radius: 8px; margin: 20px 0; border-left: 4px solid #2196F3;">
            <h2 style="margin-top: 0; color: #1565c0;">ℹ️ Defined but Unused Placeholders ({len(unused)})</h2>
            <p>These placeholders are defined in config files but not used in any template:</p>
            <div style="background-color: white; padding: 15px; border-radius: 4px; margin-top: 10px;">
                <ul style="columns: 3; -webkit-columns: 3; -moz-columns: 3; margin: 0; padding-left: 20px;">
"""
        for ph in unused:
            html += f'                    <li><code>{ph}</code></li>\n'
        
        html += """                </ul>
            </div>
            <p style="margin-top: 15px; font-size: 0.9em; color: #666;">
                <strong>Note:</strong> These placeholders may be intentionally defined for future use or for specific handbook instances. 
                Consider removing them if they are no longer needed to keep configuration files clean.
            </p>
        </div>
"""
    
    html += """
        <footer style="margin-top: 30px; padding-top: 20px; border-top: 1px solid #ddd; color: #666; text-align: center;">
            <p>Handbook Generator Placeholder Matrix</p>
        </footer>
    </div>
</body>
</html>
"""
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    
    print(f"{Colors.GREEN}HTML report generated: {output_file}{Colors.RESET}")


def main():
    """Main execution function."""
    parser = argparse.ArgumentParser(
        description='Generate placeholder coverage matrix for handbooks',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                              # Analyze all handbooks
  %(prog)s --handbook isms              # Analyze only ISMS handbook (both languages)
  %(prog)s --language de                # Analyze only German handbooks
  %(prog)s --handbook isms --language de  # Analyze only German ISMS handbook
  %(prog)s -b it-operation -l en        # Analyze only English IT Operations handbook
        """
    )
    
    parser.add_argument(
        '--handbook', '-b',
        type=str,
        help='Filter by specific handbook name (e.g., isms, it-operation, nist-csf)'
    )
    
    parser.add_argument(
        '--language', '-l',
        type=str,
        choices=['de', 'en'],
        help='Filter by language (de or en)'
    )
    
    parser.add_argument(
        '--output', '-o',
        type=str,
        default='placeholder_matrix',
        help='Output filename prefix (default: placeholder_matrix)'
    )
    
    args = parser.parse_args()
    
    # Build filter description
    filter_desc = []
    if args.handbook:
        filter_desc.append(f"handbook={args.handbook}")
    if args.language:
        filter_desc.append(f"language={args.language}")
    
    filter_str = f" ({', '.join(filter_desc)})" if filter_desc else ""
    
    print(f"{Colors.BOLD}Analyzing Handbook Placeholders{filter_str}...{Colors.RESET}")
    print(f"{Colors.YELLOW}Note: README files are excluded from analysis (they contain documentation examples){Colors.RESET}\n")
    
    # Analyze handbooks with filters
    handbook_usage, all_defined, undefined_locations = analyze_handbooks(
        handbook_filter=args.handbook,
        language_filter=args.language
    )
    
    if not handbook_usage:
        print(f"{Colors.RED}No handbooks found matching the specified filters!{Colors.RESET}")
        if args.handbook:
            print(f"\nAvailable handbooks:")
            templates_dir = Path('templates')
            for lang_dir in ['de', 'en']:
                lang_path = templates_dir / lang_dir
                if lang_path.exists():
                    handbooks = [d.name for d in lang_path.iterdir() if d.is_dir()]
                    if handbooks:
                        print(f"  {lang_dir}: {', '.join(sorted(handbooks))}")
        return
    
    # Generate output filenames with filter suffix
    suffix = ""
    if args.handbook:
        suffix += f"_{args.handbook}"
    if args.language:
        suffix += f"_{args.language}"
    
    csv_output = f"{args.output}{suffix}.csv"
    html_output = f"{args.output}{suffix}.html"
    
    # Generate matrix display
    generate_matrix(handbook_usage, all_defined)
    
    # Generate CSV report
    generate_csv_report(handbook_usage, all_defined, csv_output)
    
    # Generate HTML report
    generate_html_report(handbook_usage, all_defined, undefined_locations, html_output)
    
    print(f"\n{Colors.GREEN}Analysis complete!{Colors.RESET}")
    print(f"\n{Colors.BOLD}Open {html_output} in your browser to view the interactive report.{Colors.RESET}")


if __name__ == '__main__':
    main()
