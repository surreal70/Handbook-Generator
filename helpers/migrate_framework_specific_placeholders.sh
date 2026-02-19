#!/bin/bash
# Script to migrate framework-specific placeholders to meta-handbook format
# This converts meta.nist.*, meta.pci.*, and meta.tsc.* to meta-handbook.*

set -euo pipefail

echo "=== Framework-Specific Placeholder Migration ==="
echo ""

# NIST 800-53 placeholders
echo "Converting NIST 800-53 placeholders..."
find templates/de/nist-800-53 templates/en/nist-800-53 -type f -name "*.md" -exec sed -i 's/{{ meta\.nist\.system_id }}/{{ meta-handbook.system_id }}/g' {} +
find templates/de/nist-800-53 templates/en/nist-800-53 -type f -name "*.md" -exec sed -i 's/{{ meta\.nist\.system_name }}/{{ meta-handbook.system_name }}/g' {} +

# PCI-DSS placeholders
echo "Converting PCI-DSS placeholders..."
find templates/de/pci-dss templates/en/pci-dss -type f -name "*.md" -exec sed -i 's/{{ meta\.pci\.merchant_id }}/{{ meta-handbook.merchant_id }}/g' {} +
find templates/de/pci-dss templates/en/pci-dss -type f -name "*.md" -exec sed -i 's/{{ meta\.pci\.service_provider_id }}/{{ meta-handbook.service_provider_id }}/g' {} +

# TSC placeholders
echo "Converting TSC placeholders..."
find templates/de/tsc templates/en/tsc -type f -name "*.md" -exec sed -i 's/{{ meta\.tsc\.system_name }}/{{ meta-handbook.system_name }}/g' {} +
find templates/de/tsc templates/en/tsc -type f -name "*.md" -exec sed -i 's/{{ meta\.tsc\.report_period }}/{{ meta-handbook.report_period }}/g' {} +

echo ""
echo "=== Migration Summary ==="
echo ""

# Count conversions
nist_system_id=$(grep -r "{{ meta-handbook.system_id }}" templates/de/nist-800-53 templates/en/nist-800-53 2>/dev/null | wc -l)
nist_system_name=$(grep -r "{{ meta-handbook.system_name }}" templates/de/nist-800-53 templates/en/nist-800-53 2>/dev/null | wc -l)
pci_merchant=$(grep -r "{{ meta-handbook.merchant_id }}" templates/de/pci-dss templates/en/pci-dss 2>/dev/null | wc -l)
pci_provider=$(grep -r "{{ meta-handbook.service_provider_id }}" templates/de/pci-dss templates/en/pci-dss 2>/dev/null | wc -l)
tsc_system=$(grep -r "{{ meta-handbook.system_name }}" templates/de/tsc templates/en/tsc 2>/dev/null | wc -l)
tsc_period=$(grep -r "{{ meta-handbook.report_period }}" templates/de/tsc templates/en/tsc 2>/dev/null | wc -l)

echo "NIST 800-53:"
echo "  - system_id: $nist_system_id occurrences"
echo "  - system_name: $nist_system_name occurrences"
echo ""
echo "PCI-DSS:"
echo "  - merchant_id: $pci_merchant occurrences"
echo "  - service_provider_id: $pci_provider occurrences"
echo ""
echo "TSC:"
echo "  - system_name: $tsc_system occurrences"
echo "  - report_period: $tsc_period occurrences"
echo ""

# Verify no old-style placeholders remain
echo "Verifying no old-style placeholders remain..."
old_nist=$(grep -r "{{ meta\.nist\." templates/de/nist-800-53 templates/en/nist-800-53 2>/dev/null | wc -l)
old_pci=$(grep -r "{{ meta\.pci\." templates/de/pci-dss templates/en/pci-dss 2>/dev/null | wc -l)
old_tsc=$(grep -r "{{ meta\.tsc\." templates/de/tsc templates/en/tsc 2>/dev/null | wc -l)

if [ "$old_nist" -eq 0 ] && [ "$old_pci" -eq 0 ] && [ "$old_tsc" -eq 0 ]; then
    echo "✓ All framework-specific placeholders successfully migrated!"
else
    echo "⚠ Warning: Some old-style placeholders may remain:"
    echo "  - NIST: $old_nist"
    echo "  - PCI: $old_pci"
    echo "  - TSC: $old_tsc"
fi

echo ""
echo "Migration complete!"
