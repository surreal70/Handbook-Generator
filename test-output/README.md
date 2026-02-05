# Test Output Directory

This directory contains all generated handbook outputs when using the `--test` flag.

## Directory Structure

```
test-output/
├── de/                    # German language outputs
│   ├── markdown/          # Separate markdown files per template
│   ├── pdf/               # PDF outputs with table of contents
│   └── html/              # HTML mini-website outputs
└── en/                    # English language outputs
    ├── markdown/          # Separate markdown files per template
    ├── pdf/               # PDF outputs with table of contents
    └── html/              # HTML mini-website outputs
```

## Usage

To generate outputs to this directory, use the `--test` flag:

```bash
# Generate German BCM handbook in test mode
python -m src.cli --language de --template bcm --test

# Generate English ISMS handbook in PDF format only
python -m src.cli -l en -t isms -o pdf --test
```

## Important Notes

- **Test mode is required**: Without the `--test` flag, the system will not generate any output files to prevent accidental overwrites.
- **Consolidated structure**: All output types (markdown, PDF, HTML) are organized under this single directory structure.
- **Language separation**: Each language has its own subdirectory with separate output type folders.
- **Template type organization**: Within each output type folder, files are named with the template type prefix (e.g., `bcm_handbook.pdf`).

## Migration from Old Structure

Previously, outputs were generated to:
- `Handbook/{language}/{template-type}/` for markdown
- `PDF_Output/{language}/{template-type}/` for PDFs

The new consolidated structure simplifies output management and requires explicit test mode activation for safety.
