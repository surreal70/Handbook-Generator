#!/bin/bash
# Generate PDF versions of handbooks using Pandoc
# Requires: pandoc, texlive-latex-base, texlive-fonts-recommended

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if pandoc is installed
if ! command -v pandoc &> /dev/null; then
    echo -e "${RED}Error: pandoc is not installed${NC}"
    echo "Please install pandoc:"
    echo "  Ubuntu/Debian: sudo apt-get install pandoc texlive-latex-base texlive-fonts-recommended"
    echo "  macOS: brew install pandoc basictex"
    echo "  Or download from: https://pandoc.org/installing.html"
    exit 1
fi

echo "=== Handbook PDF Generator (Pandoc) ==="
echo ""

# Create output directory
OUTPUT_DIR="PDF_Output"
mkdir -p "$OUTPUT_DIR"

# Counter for statistics
SUCCESS_COUNT=0
FAILED_COUNT=0

# Find and convert all handbook markdown files
while IFS= read -r -d '' md_file; do
    # Get relative path
    rel_path="${md_file#Handbook/}"
    
    # Create output path
    output_dir="$OUTPUT_DIR/$(dirname "$rel_path")"
    mkdir -p "$output_dir"
    
    # Get filename without extension
    filename=$(basename "$md_file" .md)
    output_file="$output_dir/${filename}.pdf"
    
    echo -e "${YELLOW}Converting:${NC} $md_file"
    
    # Convert using pandoc with XeLaTeX for Unicode support
    if pandoc "$md_file" \
        -o "$output_file" \
        --pdf-engine=xelatex \
        -V geometry:margin=2cm \
        -V fontsize=10pt \
        -V documentclass=article \
        -V papersize=a4 \
        -V mainfont="DejaVu Sans" \
        -V monofont="DejaVu Sans Mono" \
        --toc \
        --toc-depth=3 \
        --number-sections \
        --highlight-style=tango \
        --resource-path="$(dirname "$md_file")" \
        2>/dev/null; then
        
        echo -e "${GREEN}  → Created:${NC} $output_file"
        ((SUCCESS_COUNT++))
    else
        echo -e "${RED}  ✗ Failed to convert${NC}"
        ((FAILED_COUNT++))
    fi
    echo ""
    
done < <(find Handbook -name "*_handbook.md" -type f -print0)

# Summary
echo "=== Conversion Summary ==="
echo -e "${GREEN}Successfully converted: $SUCCESS_COUNT${NC}"
if [ $FAILED_COUNT -gt 0 ]; then
    echo -e "${RED}Failed: $FAILED_COUNT${NC}"
fi
echo "Output directory: $OUTPUT_DIR/"

exit 0
