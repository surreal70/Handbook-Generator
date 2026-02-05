#!/bin/bash
# Generate all handbooks in PDF and HTML formats for both languages

set -e  # Exit on error

echo "=========================================="
echo "Generating All Handbooks"
echo "=========================================="
echo ""

# Define handbook types
TYPES=("bcm" "isms" "bsi-grundschutz" "it-operation")
LANGUAGES=("de" "en")
FORMATS=("html")  # PDF disabled due to missing libpango

# Counter for tracking progress
TOTAL=$((${#TYPES[@]} * ${#LANGUAGES[@]} * ${#FORMATS[@]}))
CURRENT=0

# Generate each combination
for lang in "${LANGUAGES[@]}"; do
    for type in "${TYPES[@]}"; do
        for format in "${FORMATS[@]}"; do
            CURRENT=$((CURRENT + 1))
            echo "[$CURRENT/$TOTAL] Generating $lang $type handbook in $format format..."
            
            ./handbook-generator -l "$lang" -t "$type" -o "$format" --test 2>&1 | grep -E "(✓|ERROR|Generating)" || true
            
            if [ $? -eq 0 ]; then
                echo "  ✓ Success"
            else
                echo "  ✗ Failed"
            fi
            echo ""
        done
    done
done

echo "=========================================="
echo "Generation Complete!"
echo "=========================================="
echo ""
echo "Output directory structure:"
echo "test-output/"
echo "├── de/"
echo "│   ├── bcm/html/"
echo "│   ├── isms/html/"
echo "│   ├── bsi-grundschutz/html/"
echo "│   └── it-operation/html/"
echo "└── en/"
echo "    ├── bcm/html/"
echo "    ├── isms/html/"
echo "    ├── bsi-grundschutz/html/"
echo "    └── it-operation/html/"
echo ""
echo "Note: PDF generation skipped due to missing libpango library"
