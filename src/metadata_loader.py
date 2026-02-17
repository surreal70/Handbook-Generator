"""
Metadata loader component for configuration separation.

This module provides the MetadataLoader class that loads and validates
metadata from separate YAML configuration files:
- meta-global.yaml: Handbook Generator version and source
- meta-organisation.yaml: Organization information
- meta-organisation-roles.yaml: Personnel roles
- meta-handbook.yaml: Handbook-specific metadata (per handbook)
"""

import yaml
from pathlib import Path
from typing import Dict, Any, Optional
import logging

from src.unified_metadata import (
    GlobalMetadata,
    OrganisationMetadata,
    RolesMetadata,
    HandbookMetadata,
    UnifiedMetadata
)

logger = logging.getLogger(__name__)


class MetadataLoader:
    """
    Loads metadata from separate YAML configuration files.
    
    Handles missing files gracefully by providing default values.
    Validates configuration structure and reports errors clearly.
    """
    
    def __init__(self, data_source_config: Optional[Dict[str, Any]] = None):
        """
        Initialize metadata loader with data source configuration.
        
        Args:
            data_source_config: Dictionary containing paths to metadata files.
                               If None or missing keys, uses default file names.
        """
        if data_source_config is None:
            data_source_config = {}
        
        # Extract metadata file paths from config, use defaults if not specified
        self.meta_global_path = Path(
            data_source_config.get('meta-global', 'meta-global.yaml')
        )
        self.meta_org_path = Path(
            data_source_config.get('meta-organisation', 'meta-organisation.yaml')
        )
        self.meta_roles_path = Path(
            data_source_config.get('meta-organisation-roles', 'meta-organisation-roles.yaml')
        )
        
        # Track loaded files to detect circular references
        self._loading_stack: list[Path] = []
    
    def _check_circular_reference(self, file_path: Path) -> None:
        """
        Check for circular file references.
        
        Args:
            file_path: Path to file being loaded
            
        Raises:
            ValueError: If circular reference is detected
        """
        # Resolve to absolute path for comparison
        abs_path = file_path.resolve()
        
        if abs_path in self._loading_stack:
            # Circular reference detected
            cycle = " -> ".join(str(p) for p in self._loading_stack)
            cycle += f" -> {abs_path}"
            error_msg = (
                f"ERROR ConfigLoader: Circular reference detected in configuration files\n"
                f"  Context: {cycle}\n"
                f"  Suggestion: Remove circular file references from your configuration. "
                f"Configuration files should not reference each other in a cycle."
            )
            logger.error(error_msg)
            raise ValueError(error_msg)
    
    def _load_yaml(self, file_path: Path) -> Optional[Dict[str, Any]]:
        """
        Safely load YAML file with enhanced error reporting.
        
        Args:
            file_path: Path to YAML file
            
        Returns:
            Parsed YAML data as dictionary, or None if file doesn't exist
            
        Raises:
            yaml.YAMLError: If YAML syntax is invalid, with enhanced error message
            ValueError: If circular reference is detected
        """
        if not file_path.exists():
            logger.warning(f"Configuration file not found: {file_path}")
            return None
        
        # Check for circular references
        abs_path = file_path.resolve()
        self._check_circular_reference(abs_path)
        
        # Add to loading stack
        self._loading_stack.append(abs_path)
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = yaml.safe_load(f)
                return data if data is not None else {}
        except yaml.YAMLError as e:
            # Extract line number if available
            line_info = ""
            if hasattr(e, 'problem_mark'):
                mark = e.problem_mark
                line_info = f" at line {mark.line + 1}, column {mark.column + 1}"
            
            error_msg = (
                f"ERROR ConfigLoader {file_path}{line_info}: Invalid YAML syntax\n"
                f"  Context: {str(e)}\n"
                f"  Suggestion: Check YAML syntax at the specified location. "
                f"Common issues include incorrect indentation, missing colons, or unquoted special characters."
            )
            logger.error(error_msg)
            raise yaml.YAMLError(error_msg) from e
        finally:
            # Remove from loading stack when done
            if abs_path in self._loading_stack:
                self._loading_stack.remove(abs_path)
    
    def _apply_defaults(self, data: Optional[Dict[str, Any]], defaults: Dict[str, Any]) -> Dict[str, Any]:
        """
        Apply default values for missing fields.
        
        Args:
            data: Loaded data dictionary (may be None)
            defaults: Default values to apply
            
        Returns:
            Dictionary with defaults applied for missing fields
        """
        if data is None:
            return defaults.copy()
        
        result = defaults.copy()
        result.update(data)
        return result

    def _validate_required_fields(self, data: Dict[str, Any], required_fields: Dict[str, type], 
                                   file_path: Path) -> None:
        """
        Validate that required fields are present in the data.
        
        Args:
            data: Loaded data dictionary
            required_fields: Dictionary mapping field names to expected types
            file_path: Path to the configuration file (for error reporting)
            
        Raises:
            ValueError: If required fields are missing
        """
        missing_fields = []
        
        for field_name, field_type in required_fields.items():
            if field_name not in data:
                missing_fields.append(field_name)
        
        if missing_fields:
            fields_str = ", ".join(f"'{field}'" for field in missing_fields)
            error_msg = (
                f"ERROR ConfigLoader {file_path}: Missing required fields: {fields_str}\n"
                f"  Context: These fields are required for proper configuration\n"
                f"  Suggestion: Add the missing fields to {file_path}. "
                f"See {file_path.stem}.example.yaml for reference."
            )
            logger.error(error_msg)
            raise ValueError(error_msg)

    def _validate_field_types(self, data: Dict[str, Any], field_types: Dict[str, type], 
                              file_path: Path) -> None:
        """
        Validate that field values match expected types.
        
        Args:
            data: Loaded data dictionary
            field_types: Dictionary mapping field names to expected types
            file_path: Path to the configuration file (for error reporting)
            
        Raises:
            TypeError: If field types don't match expected types
        """
        type_errors = []
        
        for field_name, expected_type in field_types.items():
            if field_name in data:
                actual_value = data[field_name]
                # Handle None values - they're allowed for optional fields
                if actual_value is None:
                    continue
                
                # Check type
                if not isinstance(actual_value, expected_type):
                    actual_type = type(actual_value).__name__
                    expected_type_name = expected_type.__name__
                    type_errors.append(
                        f"'{field_name}': expected {expected_type_name}, got {actual_type}"
                    )
        
        if type_errors:
            errors_str = "; ".join(type_errors)
            error_msg = (
                f"ERROR ConfigLoader {file_path}: Field type mismatches: {errors_str}\n"
                f"  Context: Field values must match their expected types\n"
                f"  Suggestion: Correct the field types in {file_path}. "
                f"See {file_path.stem}.example.yaml for reference."
            )
            logger.error(error_msg)
            raise TypeError(error_msg)

    
    def _load_global_metadata(self) -> GlobalMetadata:
        """
        Load global metadata from meta-global.yaml.
        
        Applies defaults:
        - source: "HandBook Generator"
        - version: "1.0.0"
        
        Returns:
            GlobalMetadata object with loaded or default values
        """
        defaults = {
            'source': 'HandBook Generator',
            'version': '1.0.0'
        }
        
        # Define required fields and their types
        field_types = {
            'source': str,
            'version': str
        }
        
        data = self._load_yaml(self.meta_global_path)
        
        # Only validate if data was loaded (not using defaults)
        if data is not None and data:
            self._validate_field_types(data, field_types, self.meta_global_path)
        
        merged = self._apply_defaults(data, defaults)
        
        return GlobalMetadata(
            source=merged['source'],
            version=merged['version']
        )

    
    def _load_organisation_metadata(self) -> OrganisationMetadata:
        """
        Load organisation metadata from meta-organisation.yaml.
        
        Applies defaults:
        - name: "[TODO]"
        - address: "[TODO]"
        - web: "[TODO]"
        - phone: "[TODO]"
        - revision: 0
        
        Returns:
            OrganisationMetadata object with loaded or default values
        """
        defaults = {
            'name': '[TODO]',
            'address': '[TODO]',
            'web': '[TODO]',
            'phone': '[TODO]',
            'revision': 0
        }
        
        # Define field types
        field_types = {
            'name': str,
            'address': str,
            'web': str,
            'phone': str,
            'revision': int
        }
        
        data = self._load_yaml(self.meta_org_path)
        
        # Only validate if data was loaded (not using defaults)
        if data is not None and data:
            self._validate_field_types(data, field_types, self.meta_org_path)
        
        merged = self._apply_defaults(data, defaults)
        
        return OrganisationMetadata(
            name=merged['name'],
            address=merged['address'],
            web=merged['web'],
            phone=merged['phone'],
            revision=merged['revision']
        )

    
    def _load_roles_metadata(self) -> RolesMetadata:
        """
        Load roles metadata from meta-organisation-roles.yaml.
        
        Applies defaults: all role fields default to "[TODO]"
        Validates that role identifiers use English names (role_CEO not rolle_CEO)
        
        Returns:
            RolesMetadata object with loaded or default values
            
        Raises:
            ValueError: If non-English role identifiers are detected
        """
        defaults = {
            'role_CEO': '[TODO]',
            'role_CFO': '[TODO]',
            'role_CTO': '[TODO]',
            'role_CIO': '[TODO]',
            'role_CISO': '[TODO]',
            'role_HR_Manager': '[TODO]',
            'role_Risk_Manager': '[TODO]',
            'role_GDPR_Manager': '[TODO]',
            'role_IT_Manager': '[TODO]',
            'role_Compliance_Manager': '[TODO]',
            'role_Internal_Auditor': '[TODO]',
            'group_IT_Services': '[TODO]',
            'group_DEVOPS': '[TODO]',
            'group_Helpdesk': '[TODO]'
        }
        
        # Define field types (all roles are strings)
        field_types = {key: str for key in defaults.keys()}
        
        data = self._load_yaml(self.meta_roles_path)
        
        # Validate English role identifiers if data was loaded
        if data is not None:
            # Check for common German role prefixes
            german_prefixes = ['rolle_', 'gruppe_']
            for key in data.keys():
                for prefix in german_prefixes:
                    if key.lower().startswith(prefix):
                        raise ValueError(
                            f"Non-English role identifier detected: '{key}' in {self.meta_roles_path}. "
                            f"Role identifiers must use English names (e.g., 'role_CEO' not 'rolle_CEO')"
                        )
        
        # Only validate types if data was loaded (not using defaults)
        if data is not None and data:
            self._validate_field_types(data, field_types, self.meta_roles_path)
        
        merged = self._apply_defaults(data, defaults)
        
        return RolesMetadata(
            role_CEO=merged['role_CEO'],
            role_CFO=merged['role_CFO'],
            role_CTO=merged['role_CTO'],
            role_CIO=merged['role_CIO'],
            role_CISO=merged['role_CISO'],
            role_HR_Manager=merged['role_HR_Manager'],
            role_Risk_Manager=merged['role_Risk_Manager'],
            role_GDPR_Manager=merged['role_GDPR_Manager'],
            role_IT_Manager=merged['role_IT_Manager'],
            role_Compliance_Manager=merged['role_Compliance_Manager'],
            role_Internal_Auditor=merged['role_Internal_Auditor'],
            group_IT_Services=merged['group_IT_Services'],
            group_DEVOPS=merged['group_DEVOPS'],
            group_Helpdesk=merged['group_Helpdesk']
        )

    
    def load_handbook_metadata(self, handbook_path: Path) -> HandbookMetadata:
        """
        Load handbook-specific metadata from handbook directory.
        
        Looks for meta-handbook.yaml in the handbook directory.
        Applies defaults: all fields default to "[TODO]", revision=0, maintainer=author
        
        Args:
            handbook_path: Path to handbook directory
            
        Returns:
            HandbookMetadata object with loaded or default values
        """
        meta_handbook_path = handbook_path / "meta-handbook.yaml"
        
        defaults = {
            'author': '[TODO]',
            'classification': '[TODO]',
            'status': '[TODO]',
            'type': '[TODO]',
            'templateset_version': '0.1',
            'revision': 0,
            'shortname': '[TODO]',
            'longname': '[TODO]',
            'maintainer': None,  # Will be set to author in __post_init__
            'owner': '[TODO]',
            'approver': '[TODO]',
            'creationdate': '[TODO]',
            'modifydate': '[TODO]',
            'valid_from': '[TODO]',
            'next_review': '[TODO]',
            'scope': '[TODO]'
        }
        
        # Define field types
        field_types = {
            'author': str,
            'classification': str,
            'status': str,
            'type': str,
            'templateset_version': str,
            'revision': int,
            'shortname': str,
            'longname': str,
            'maintainer': str,
            'owner': str,
            'approver': str,
            'creationdate': str,
            'modifydate': str,
            'valid_from': str,
            'next_review': str,
            'scope': str
        }
        
        data = self._load_yaml(meta_handbook_path)
        
        # Warn if file is missing
        if data is None:
            logger.warning(
                f"Handbook metadata file not found: {meta_handbook_path}. "
                f"Using default values."
            )
        
        # Only validate types if data was loaded (not using defaults)
        if data is not None and data:
            self._validate_field_types(data, field_types, meta_handbook_path)
        
        merged = self._apply_defaults(data, defaults)
        
        return HandbookMetadata(
            author=merged['author'],
            classification=merged['classification'],
            status=merged['status'],
            type=merged['type'],
            templateset_version=merged['templateset_version'],
            revision=merged['revision'],
            shortname=merged['shortname'],
            longname=merged['longname'],
            maintainer=merged['maintainer'],
            owner=merged['owner'],
            approver=merged['approver'],
            creationdate=merged['creationdate'],
            modifydate=merged['modifydate'],
            valid_from=merged['valid_from'],
            next_review=merged['next_review'],
            scope=merged['scope']
        )

    
    def load_all_metadata(self) -> UnifiedMetadata:
        """
        Load and merge all global metadata files.
        
        Loads:
        - meta-global.yaml
        - meta-organisation.yaml
        - meta-organisation-roles.yaml
        
        Returns:
            UnifiedMetadata object with all global metadata sources
        """
        global_meta = self._load_global_metadata()
        org_meta = self._load_organisation_metadata()
        roles_meta = self._load_roles_metadata()
        
        return UnifiedMetadata(
            global_info=global_meta,
            organisation=org_meta,
            roles=roles_meta
        )
