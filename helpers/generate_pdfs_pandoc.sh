#!/bin/bash
# Generate PDFs from markdown files using Pandoc

set -e

echo "=========================================="
echo "Generating PDFs using Pandoc"
echo "=========================================="
echo ""

TYPES=("bcm" "isms" "bsi-grundschutz" "it-operation" "cis-controls")
LANGUAGES=("de" "en")

# First, generate separate markdown files
echo "Step 1: Generating separate markdown files..."
echo ""

for lang in "${LANGUAGES[@]}"; do
    for type in "${TYPES[@]}"; do
        echo "Generating $lang $type markdown..."
        ./handbook-generator -l "$lang" -t "$type" -o markdown --test --separate-files 2>&1 | grep -E "(✓|ERROR)" || true
    done
done

echo ""
echo "Step 2: Combining markdown files and converting to PDF..."
echo ""

# Convert each handbook to PDF
for lang in "${LANGUAGES[@]}"; do
    for type in "${TYPES[@]}"; do
        MD_DIR="test-output/$lang/$type/markdown"
        PDF_DIR="test-output/$lang/$type/pdf"
        COMBINED_MD="$MD_DIR/combined_${type}_${lang}.md"
        PDF_FILE="$PDF_DIR/${type}_handbook_${lang}.pdf"
        
        if [ -d "$MD_DIR" ]; then
            echo "Processing $lang $type..."
            mkdir -p "$PDF_DIR"
            
            # Combine all markdown files (excluding TOC.md and README)
            > "$COMBINED_MD"
            for md_file in "$MD_DIR"/[0-9]*.md; do
                if [ -f "$md_file" ]; then
                    cat "$md_file" >> "$COMBINED_MD"
                    echo -e "\n\n\\newpage\n\n" >> "$COMBINED_MD"
                fi
            done
            
            # Convert to PDF
            if [ -f "$COMBINED_MD" ]; then
                pandoc "$COMBINED_MD" \
                    -o "$PDF_FILE" \
                    --pdf-engine=xelatex \
                    --toc \
                    --toc-depth=2 \
                    --number-sections \
                    -V geometry:margin=2.5cm \
                    -V fontsize=11pt \
                    -V documentclass=report \
                    2>&1 | grep -v "WARNING" || true
                
                if [ -f "$PDF_FILE" ]; then
                    SIZE=$(du -h "$PDF_FILE" | cut -f1)
                    echo "  ✓ Created: $PDF_FILE ($SIZE)"
                    # Clean up combined markdown
                    rm "$COMBINED_MD"
                else
                    echo "  ✗ Failed to create PDF"
                fi
            fi
        else
            echo "  ✗ Markdown directory not found: $MD_DIR"
        fi
        echo ""
    done
done

echo "=========================================="
echo "PDF Generation Complete!"
echo "=========================================="
echo ""
echo "Generated PDFs:"
find test-output -name "*.pdf" -type f | sort
echo ""
echo "Total PDFs: $(find test-output -name "*.pdf" -type f | wc -l)"
echo ""
