#!/bin/bash
# migrate_placeholders.sh - Migrate placeholder format from {{ }} to [[ ]]
# Usage: ./migrate_placeholders.sh <handbook_path>
# Example: ./migrate_placeholders.sh templates/de/bcm

set -euo pipefail

HANDBOOK_PATH="${1:-}"

if [ -z "$HANDBOOK_PATH" ]; then
    echo "Usage: $0 <handbook_path>"
    echo "Example: $0 templates/de/bcm"
    echo ""
    echo "Or migrate all handbooks:"
    echo "  $0 all"
    exit 1
fi

# Function to migrate a single handbook
migrate_handbook() {
    local path="$1"
    
    if [ ! -d "$path" ]; then
        echo "Error: Directory $path does not exist"
        return 1
    fi
    
    echo "Migrating placeholders in: $path"
    
    # Count occurrences before migration
    local count_before=$(find "$path" -name "*.md" -type f -exec grep -o "{{" {} + 2>/dev/null | wc -l || echo 0)
    
    # Find and replace {{ }} with [[ ]]
    # This handles both {{ placeholder }} and {{placeholder}}
    find "$path" -name "*.md" -type f -exec sed -i 's/{{\s*/[[/g; s/\s*}}/]]/g' {} +
    
    # Count occurrences after migration
    local count_after=$(find "$path" -name "*.md" -type f -exec grep -o "{{" {} + 2>/dev/null | wc -l || echo 0)
    
    echo "  ✓ Migrated $count_before placeholder instances"
    
    if [ "$count_after" -gt 0 ]; then
        echo "  ⚠ Warning: $count_after instances of {{ still remain"
    fi
    
    echo ""
}

# Migrate all handbooks
if [ "$HANDBOOK_PATH" = "all" ]; then
    echo "Migrating all handbooks..."
    echo ""
    
    for lang in de en; do
        for framework in templates/$lang/*/; do
            if [ -d "$framework" ]; then
                migrate_handbook "$framework"
            fi
        done
    done
    
    echo "✓ All handbooks migrated"
    echo ""
    echo "Please verify the changes:"
    echo "  git diff"
    echo ""
    echo "Then commit if everything looks good:"
    echo "  git add templates/"
    echo "  git commit -m 'Migrate placeholder format from {{ }} to [[ ]]'"
else
    migrate_handbook "$HANDBOOK_PATH"
    
    echo "Migration completed for $HANDBOOK_PATH"
    echo ""
    echo "Please verify the changes:"
    echo "  git diff $HANDBOOK_PATH"
    echo ""
    echo "Then commit if everything looks good:"
    echo "  git add $HANDBOOK_PATH"
    echo "  git commit -m 'Migrate placeholder format in $(basename $HANDBOOK_PATH)'"
fi
