#!/bin/bash
# Generate PDF versions of handbooks using Pandoc with HTML intermediate
# Requires: pandoc, wkhtmltopdf

set -euo pipefail

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if pandoc is installed
if ! command -v pandoc &> /dev/null; then
    echo -e "${RED}Error: pandoc is not installed${NC}"
    echo "Please install pandoc:"
    echo "  Ubuntu/Debian: sudo apt-get install pandoc"
    echo "  macOS: brew install pandoc"
    exit 1
fi

# Check if wkhtmltopdf is installed
if ! command -v wkhtmltopdf &> /dev/null; then
    echo -e "${RED}Error: wkhtmltopdf is not installed${NC}"
    echo "Please install wkhtmltopdf:"
    echo "  Ubuntu/Debian: sudo apt-get install wkhtmltopdf"
    echo "  macOS: brew install wkhtmltopdf"
    exit 1
fi

echo -e "${BLUE}=== Handbook PDF Generator ===${NC}"
echo ""

# Create output directory
OUTPUT_DIR="PDF_Output"
mkdir -p "$OUTPUT_DIR"

# Counter for statistics
SUCCESS_COUNT=0
FAILED_COUNT=0
TOTAL_COUNT=0

# Find all handbook markdown files
mapfile -d '' handbook_files < <(find Handbook -name "*_handbook.md" -type f -print0 2>/dev/null)

TOTAL_COUNT=${#handbook_files[@]}

if [ $TOTAL_COUNT -eq 0 ]; then
    echo -e "${YELLOW}No handbook files found in Handbook/ directory${NC}"
    exit 0
fi

echo -e "${BLUE}Found $TOTAL_COUNT handbook(s) to convert${NC}"
echo ""

# Convert each handbook
for md_file in "${handbook_files[@]}"; do
    # Get relative path
    rel_path="${md_file#Handbook/}"
    
    # Create output path
    output_dir="$OUTPUT_DIR/$(dirname "$rel_path")"
    mkdir -p "$output_dir"
    
    # Get filename without extension
    filename=$(basename "$md_file" .md)
    output_file="$output_dir/${filename}.pdf"
    temp_html="${output_file%.pdf}.html"
    
    echo -e "${YELLOW}Converting:${NC} $md_file"
    
    # Step 1: Convert Markdown to HTML with Pandoc
    if pandoc "$md_file" \
        -o "$temp_html" \
        --standalone \
        --toc \
        --toc-depth=3 \
        --number-sections \
        --highlight-style=tango \
        --css=<(cat <<'EOF'
body {
    font-family: Arial, sans-serif;
    font-size: 10pt;
    line-height: 1.6;
    color: #333;
    max-width: 210mm;
    margin: 0 auto;
    padding: 20px;
}
h1 {
    color: #2c3e50;
    font-size: 24pt;
    margin-top: 20pt;
    margin-bottom: 12pt;
    page-break-after: avoid;
}
h2 {
    color: #34495e;
    font-size: 18pt;
    margin-top: 16pt;
    margin-bottom: 10pt;
    page-break-after: avoid;
}
h3 {
    color: #555;
    font-size: 14pt;
    margin-top: 12pt;
    margin-bottom: 8pt;
    page-break-after: avoid;
}
h4 {
    color: #666;
    font-size: 12pt;
    margin-top: 10pt;
    margin-bottom: 6pt;
}
code {
    background-color: #f4f4f4;
    padding: 2px 4px;
    border-radius: 3px;
    font-family: monospace;
    font-size: 9pt;
}
pre {
    background-color: #f4f4f4;
    padding: 10pt;
    border-radius: 5px;
    border-left: 3px solid #3498db;
    overflow-x: auto;
    page-break-inside: avoid;
}
table {
    border-collapse: collapse;
    width: 100%;
    margin: 10pt 0;
    page-break-inside: avoid;
}
th, td {
    border: 1px solid #ddd;
    padding: 8pt;
    text-align: left;
}
th {
    background-color: #3498db;
    color: white;
    font-weight: bold;
}
tr:nth-child(even) {
    background-color: #f9f9f9;
}
#TOC {
    background-color: #f8f9fa;
    padding: 15pt;
    border-radius: 5px;
    margin-bottom: 20pt;
}
EOF
) \
        --metadata title="$(basename "$filename" | sed 's/_/ /g')" \
        2>/dev/null; then
        
        # Step 2: Convert HTML to PDF with wkhtmltopdf
        if wkhtmltopdf \
            --page-size A4 \
            --margin-top 20mm \
            --margin-right 20mm \
            --margin-bottom 20mm \
            --margin-left 20mm \
            --encoding UTF-8 \
            --enable-local-file-access \
            --footer-center "[page]/[topage]" \
            --footer-font-size 9 \
            "$temp_html" \
            "$output_file" \
            2>/dev/null; then
            
            echo -e "${GREEN}  → Created:${NC} $output_file"
            ((SUCCESS_COUNT++))
            
            # Clean up temporary HTML
            rm -f "$temp_html"
        else
            echo -e "${RED}  ✗ Failed to convert HTML to PDF${NC}"
            ((FAILED_COUNT++))
        fi
    else
        echo -e "${RED}  ✗ Failed to convert Markdown to HTML${NC}"
        ((FAILED_COUNT++))
    fi
    echo ""
done

# Summary
echo -e "${BLUE}=== Conversion Summary ===${NC}"
echo -e "${GREEN}Successfully converted: $SUCCESS_COUNT${NC}"
if [ $FAILED_COUNT -gt 0 ]; then
    echo -e "${RED}Failed: $FAILED_COUNT${NC}"
fi
echo -e "${BLUE}Output directory: $OUTPUT_DIR/${NC}"

if [ $FAILED_COUNT -gt 0 ]; then
    exit 1
fi

exit 0
