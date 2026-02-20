#!/bin/bash
# Generate all handbooks in both languages
# Markdown: separate files per template
# PDF: single combined file

set -euo pipefail

# Color codes for output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# List of all handbooks
HANDBOOKS=(
    "bcm"
    "bsi-grundschutz"
    "cis-controls"
    "common-criteria"
    "coso"
    "csa-ccm"
    "dora"
    "gdpr"
    "hipaa"
    "idw-ps-951"
    "isms"
    "iso-31000"
    "iso-38500"
    "iso-9001"
    "it-operation"
    "nist-800-53"
    "nist-csf"
    "pci-dss"
    "soc1"
    "tisax"
    "togaf"
    "tsc"
)

LANGUAGES=("de" "en")

# Statistics
TOTAL_HANDBOOKS=$((${#HANDBOOKS[@]} * ${#LANGUAGES[@]}))
CURRENT=0
SUCCESS=0
FAILED=0
FAILED_LIST=()

echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Handbook Generator - Batch Processing${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""
echo "Generating ${TOTAL_HANDBOOKS} handbooks (${#HANDBOOKS[@]} types × ${#LANGUAGES[@]} languages)"
echo "Output format: Markdown (separate files)"
echo "Note: PDF generation requires system libraries (libpango) - skipped for now"
echo ""

START_TIME=$(date +%s)

# Generate each handbook
for lang in "${LANGUAGES[@]}"; do
    echo -e "\n${YELLOW}Processing language: ${lang}${NC}"
    echo "----------------------------------------"
    
    for handbook in "${HANDBOOKS[@]}"; do
        CURRENT=$((CURRENT + 1))
        
        echo -ne "${BLUE}[${CURRENT}/${TOTAL_HANDBOOKS}]${NC} Generating ${lang}/${handbook}... "
        
        # Run handbook generator (markdown only for now, PDF requires system libraries)
        if python3 handbook-generator \
            --template "${handbook}" \
            --language "${lang}" \
            --output markdown \
            --separate-files \
            --test \
            > /dev/null 2>&1; then
            
            echo -e "${GREEN}✓${NC}"
            SUCCESS=$((SUCCESS + 1))
        else
            echo -e "${RED}✗${NC}"
            FAILED=$((FAILED + 1))
            FAILED_LIST+=("${lang}/${handbook}")
        fi
    done
done

END_TIME=$(date +%s)
DURATION=$((END_TIME - START_TIME))

# Print summary
echo ""
echo -e "${BLUE}========================================${NC}"
echo -e "${BLUE}Generation Summary${NC}"
echo -e "${BLUE}========================================${NC}"
echo ""
echo "Total handbooks:  ${TOTAL_HANDBOOKS}"
echo -e "Successful:       ${GREEN}${SUCCESS}${NC}"
echo -e "Failed:           ${RED}${FAILED}${NC}"
echo "Duration:         ${DURATION} seconds"
echo ""

if [ ${FAILED} -gt 0 ]; then
    echo -e "${RED}Failed handbooks:${NC}"
    for failed in "${FAILED_LIST[@]}"; do
        echo "  - ${failed}"
    done
    echo ""
fi

# Show output structure
echo -e "${BLUE}Output Structure:${NC}"
echo "test-output/"
echo "├── de/"
echo "│   ├── bcm/"
echo "│   │   └── markdown/     (separate .md files)"
echo "│   ├── isms/"
echo "│   │   └── markdown/"
echo "│   └── ..."
echo "└── en/"
echo "    └── ..."
echo ""

if [ ${FAILED} -eq 0 ]; then
    echo -e "${GREEN}✓ All handbooks generated successfully!${NC}"
    exit 0
else
    echo -e "${YELLOW}⚠ Some handbooks failed to generate.${NC}"
    exit 1
fi
