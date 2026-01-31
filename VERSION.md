# Version Management

## Current Version: 0.0.1

### Single Source of Truth

The version number for this project is defined in **one place only**:

```
src/__init__.py
```

This file contains the `__version__` variable which is the authoritative source for the project version.

### How Version is Used

All other parts of the codebase reference this single source:

1. **setup.py**: Imports `__version__` from `src/__init__.py` for package distribution
2. **config_manager.py**: Uses `__version__` as default fallback for metadata version
3. **placeholder_processor.py**: Uses `__version__` as default fallback for document version
4. **metadata_config_manager.py**: Uses version "0.0.1" as default for document metadata

### Updating the Version

To update the version number:

1. Edit `src/__init__.py`
2. Change the `__version__` value
3. All other references will automatically use the new version

**Do not** hardcode version numbers elsewhere in the codebase.

### Version History

- **0.0.1** (2025-01-31): Initial experimental release
  - Early development state
  - Highly experimental
  - Not production ready
