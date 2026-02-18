"""
Tests for Configuration Manager

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025, 2026
"""

import pytest
import yaml
from pathlib import Path
from hypothesis import given, strategies as st
from tempfile import TemporaryDirectory

from src.config_manager import Config, ConfigManager, DataSourceConfig


# Hypothesis strategies for generating test data
@st.composite
def data_source_config_strategy(draw):
    """Generate valid data source configuration."""
    url = draw(st.text(min_size=1, alphabet=st.characters(blacklist_characters=['\n', '\r'])))
    api_token = draw(st.text(min_size=1, alphabet=st.characters(blacklist_characters=['\n', '\r'])))
    return {'url': url, 'api_token': api_token}


@st.composite
def config_dict_strategy(draw):
    """Generate valid configuration dictionary."""
    # Generate at least one data source
    num_sources = draw(st.integers(min_value=1, max_value=3))
    data_sources = {}
    
    for i in range(num_sources):
        source_name = draw(st.text(
            min_size=1, 
            max_size=20,
            alphabet=st.characters(whitelist_categories=('Ll', 'Lu', 'Nd'), blacklist_characters=['\n', '\r'])
        ))
        if source_name:  # Ensure non-empty
            data_sources[source_name] = draw(data_source_config_strategy())
    
    # Ensure we have at least one data source
    if not data_sources:
        data_sources['netbox'] = {
            'url': 'https://example.com',
            'api_token': 'token123'
        }
    
    config = {
        'data_sources': data_sources,
        'defaults': {
            'language': draw(st.sampled_from(['de', 'en'])),
            'output_format': draw(st.sampled_from(['markdown', 'pdf', 'both']))
        },
        'metadata': {
            'author': draw(st.text(min_size=1, max_size=100)),
            'version': draw(st.text(min_size=1, max_size=20))
        }
    }
    
    return config


@pytest.mark.property
@given(config_dict=config_dict_strategy())
def test_property_9_configuration_parsing(config_dict):
    """
    Feature: handbook-generator, Property 9: Configuration Parsing
    
    For any valid configuration file containing data source credentials,
    the system should correctly extract all connection parameters
    (URL, API tokens, etc.).
    
    Validates: Requirements 5.3
    """
    with TemporaryDirectory() as tmpdir:
        config_path = Path(tmpdir) / 'config.yaml'
        
        # Write configuration to file
        with open(config_path, 'w', encoding='utf-8') as f:
            yaml.dump(config_dict, f)
        
        # Load configuration
        manager = ConfigManager(config_path)
        config = manager.load_config()
        
        # Verify all data sources are parsed correctly
        assert len(config.data_sources) == len(config_dict['data_sources'])
        
        for source_name, source_config in config_dict['data_sources'].items():
            assert source_name in config.data_sources
            parsed_source = config.data_sources[source_name]
            assert isinstance(parsed_source, DataSourceConfig)
            assert parsed_source.url == source_config['url']
            assert parsed_source.api_token == source_config['api_token']
        
        # Verify defaults are parsed correctly
        assert config.default_language == config_dict['defaults']['language']
        assert config.default_output_format == config_dict['defaults']['output_format']
        
        # Verify metadata is parsed correctly
        assert config.author == config_dict['metadata']['author']
        assert config.version == config_dict['metadata']['version']


@pytest.mark.property
@given(config_dict=config_dict_strategy())
def test_property_22_multi_source_configuration_support(config_dict):
    """
    Feature: handbook-generator, Property 22: Multi-Source Configuration Support
    
    For any configuration file containing credentials for multiple data sources,
    the system should correctly parse and store all data source configurations.
    
    Validates: Requirements 11.5
    """
    with TemporaryDirectory() as tmpdir:
        config_path = Path(tmpdir) / 'config.yaml'
        
        # Write configuration to file
        with open(config_path, 'w', encoding='utf-8') as f:
            yaml.dump(config_dict, f)
        
        # Load configuration
        manager = ConfigManager(config_path)
        config = manager.load_config()
        
        # Verify all data sources are present
        assert len(config.data_sources) >= 1
        assert len(config.data_sources) == len(config_dict['data_sources'])
        
        # Verify each data source is correctly configured
        for source_name in config_dict['data_sources'].keys():
            assert source_name in config.data_sources
            source = config.data_sources[source_name]
            assert isinstance(source, DataSourceConfig)
            assert source.url is not None
            assert source.api_token is not None
            assert len(source.url) > 0
            assert len(source.api_token) > 0


# Unit tests for error handling


@pytest.mark.unit
def test_missing_config_file():
    """
    Test für fehlende Konfigurationsdatei
    
    Requirements: 5.5
    """
    with TemporaryDirectory() as tmpdir:
        config_path = Path(tmpdir) / 'nonexistent.yaml'
        manager = ConfigManager(config_path)
        
        with pytest.raises(FileNotFoundError) as exc_info:
            manager.load_config()
        
        assert 'Configuration file not found' in str(exc_info.value)
        assert str(config_path) in str(exc_info.value)


@pytest.mark.unit
def test_invalid_yaml_syntax():
    """
    Test für ungültige YAML-Syntax
    
    Requirements: 5.5
    """
    with TemporaryDirectory() as tmpdir:
        config_path = Path(tmpdir) / 'invalid.yaml'
        
        # Write invalid YAML
        with open(config_path, 'w', encoding='utf-8') as f:
            f.write("data_sources:\n  netbox:\n    url: [invalid yaml structure")
        
        manager = ConfigManager(config_path)
        
        with pytest.raises(yaml.YAMLError) as exc_info:
            manager.load_config()
        
        assert 'Invalid YAML syntax' in str(exc_info.value)


@pytest.mark.unit
def test_missing_required_url_field():
    """
    Test für fehlende Pflichtfelder - URL
    
    Requirements: 5.5
    """
    with TemporaryDirectory() as tmpdir:
        config_path = Path(tmpdir) / 'config.yaml'
        
        # Configuration missing URL
        config_dict = {
            'data_sources': {
                'netbox': {
                    'api_token': 'token123'
                    # Missing 'url'
                }
            }
        }
        
        with open(config_path, 'w', encoding='utf-8') as f:
            yaml.dump(config_dict, f)
        
        manager = ConfigManager(config_path)
        
        with pytest.raises(ValueError) as exc_info:
            manager.load_config()
        
        assert "Missing required field 'url'" in str(exc_info.value)
        assert 'netbox' in str(exc_info.value)


@pytest.mark.unit
def test_missing_required_api_token_field():
    """
    Test für fehlende Pflichtfelder - API Token
    
    Requirements: 5.5
    """
    with TemporaryDirectory() as tmpdir:
        config_path = Path(tmpdir) / 'config.yaml'
        
        # Configuration missing API token
        config_dict = {
            'data_sources': {
                'netbox': {
                    'url': 'https://netbox.example.com'
                    # Missing 'api_token'
                }
            }
        }
        
        with open(config_path, 'w', encoding='utf-8') as f:
            yaml.dump(config_dict, f)
        
        manager = ConfigManager(config_path)
        
        with pytest.raises(ValueError) as exc_info:
            manager.load_config()
        
        assert "Missing required field 'api_token'" in str(exc_info.value)
        assert 'netbox' in str(exc_info.value)


@pytest.mark.unit
def test_empty_config_file():
    """
    Test für leere Konfigurationsdatei
    
    Requirements: 5.5
    """
    with TemporaryDirectory() as tmpdir:
        config_path = Path(tmpdir) / 'empty.yaml'
        
        # Write empty file
        with open(config_path, 'w', encoding='utf-8') as f:
            f.write('')
        
        manager = ConfigManager(config_path)
        
        with pytest.raises(ValueError) as exc_info:
            manager.load_config()
        
        assert 'Configuration file is empty' in str(exc_info.value)


@pytest.mark.unit
def test_create_default_config():
    """Test default configuration creation."""
    with TemporaryDirectory() as tmpdir:
        config_path = Path(tmpdir) / 'config.yaml'
        manager = ConfigManager(config_path)
        
        # Create default config
        manager.create_default_config()
        
        # Verify file was created
        assert config_path.exists()
        
        # Verify content is valid YAML
        with open(config_path, 'r', encoding='utf-8') as f:
            content = f.read()
            assert 'data_sources:' in content
            assert 'netbox:' in content
            assert 'WARNING' in content


@pytest.mark.unit
def test_create_default_config_already_exists():
    """Test that creating default config fails if file exists."""
    with TemporaryDirectory() as tmpdir:
        config_path = Path(tmpdir) / 'config.yaml'
        
        # Create file first
        with open(config_path, 'w', encoding='utf-8') as f:
            f.write('existing content')
        
        manager = ConfigManager(config_path)
        
        with pytest.raises(FileExistsError) as exc_info:
            manager.create_default_config()
        
        assert 'already exists' in str(exc_info.value)


@pytest.mark.unit
def test_ensure_gitignore():
    """Test gitignore management."""
    with TemporaryDirectory() as tmpdir:
        # Create a fake git repo
        git_dir = Path(tmpdir) / '.git'
        git_dir.mkdir()
        
        config_path = Path(tmpdir) / 'config.yaml'
        manager = ConfigManager(config_path)
        
        # Ensure gitignore
        manager.ensure_gitignore()
        
        gitignore_path = Path(tmpdir) / '.gitignore'
        assert gitignore_path.exists()
        
        with open(gitignore_path, 'r', encoding='utf-8') as f:
            content = f.read()
            assert 'config.yaml' in content


@pytest.mark.unit
def test_ensure_gitignore_already_present():
    """Test that gitignore doesn't duplicate entries."""
    with TemporaryDirectory() as tmpdir:
        # Create a fake git repo
        git_dir = Path(tmpdir) / '.git'
        git_dir.mkdir()
        
        config_path = Path(tmpdir) / 'config.yaml'
        gitignore_path = Path(tmpdir) / '.gitignore'
        
        # Create gitignore with config already in it
        with open(gitignore_path, 'w', encoding='utf-8') as f:
            f.write('config.yaml\n')
        
        manager = ConfigManager(config_path)
        manager.ensure_gitignore()
        
        # Verify no duplication
        with open(gitignore_path, 'r', encoding='utf-8') as f:
            content = f.read()
            assert content.count('config.yaml') == 1


@pytest.mark.unit
def test_config_netbox_properties():
    """Test Config netbox convenience properties."""
    config = Config(
        data_sources={
            'netbox': DataSourceConfig(
                url='https://netbox.test.com',
                api_token='test_token'
            )
        }
    )
    
    assert config.netbox_url == 'https://netbox.test.com'
    assert config.netbox_api_token == 'test_token'


@pytest.mark.unit
def test_config_netbox_properties_missing():
    """Test Config netbox properties when netbox is not configured."""
    config = Config(data_sources={})
    
    assert config.netbox_url is None
    assert config.netbox_api_token is None



@pytest.mark.property
@given(
    missing_url=st.booleans(),
    missing_token=st.booleans(),
    invalid_url=st.booleans(),
    placeholder_token=st.booleans(),
    invalid_format=st.booleans()
)
def test_property_10_invalid_configuration_handling(
    missing_url, missing_token, invalid_url, placeholder_token, invalid_format
):
    """
    Feature: handbook-generator, Property 10: Invalid Configuration Handling
    
    For any configuration file with missing or invalid credentials,
    the system should generate a descriptive error message indicating
    which fields are problematic.
    
    Validates: Requirements 5.5
    """
    # Skip if no errors are introduced
    if not any([missing_url, missing_token, invalid_url, placeholder_token, invalid_format]):
        return
    
    with TemporaryDirectory() as tmpdir:
        config_path = Path(tmpdir) / 'config.yaml'
        
        # Build configuration with intentional errors
        config_dict = {
            'data_sources': {
                'netbox': {}
            },
            'defaults': {
                'language': 'de',
                'output_format': 'both' if not invalid_format else 'invalid_format'
            },
            'metadata': {
                'author': 'Test Author',
                'version': '1.0.0'
            }
        }
        
        # Add URL field (or not)
        if not missing_url:
            if invalid_url:
                config_dict['data_sources']['netbox']['url'] = 'not-a-valid-url'
            else:
                config_dict['data_sources']['netbox']['url'] = 'https://netbox.example.com'
        
        # Add API token field (or not)
        if not missing_token:
            if placeholder_token:
                config_dict['data_sources']['netbox']['api_token'] = 'your-api-token-here'
            else:
                config_dict['data_sources']['netbox']['api_token'] = 'valid_token_123'
        
        # Write configuration to file
        with open(config_path, 'w', encoding='utf-8') as f:
            yaml.dump(config_dict, f)
        
        manager = ConfigManager(config_path)
        
        # Try to load configuration
        try:
            config = manager.load_config()
            
            # If we got here, validate the config
            error_msg = manager.validate_config(config)
            
            # Should have an error message if there are issues
            if any([invalid_url, placeholder_token, invalid_format]):
                assert error_msg is not None, "Expected validation error but got none"
                assert 'Configuration error' in error_msg
                
                # Check that specific issues are mentioned
                if invalid_url:
                    assert 'url' in error_msg.lower()
                if placeholder_token:
                    assert 'api_token' in error_msg.lower() or 'token' in error_msg.lower()
                if invalid_format:
                    assert 'output_format' in error_msg.lower() or 'format' in error_msg.lower()
            
        except ValueError as e:
            # Loading failed due to missing required fields
            error_msg = str(e)
            
            # Verify error message is descriptive
            assert len(error_msg) > 0, "Error message should not be empty"
            
            # Check that at least one of the missing fields is mentioned
            # (the parser stops at the first missing field)
            if missing_url or missing_token:
                assert 'url' in error_msg.lower() or 'api_token' in error_msg.lower() or 'token' in error_msg.lower()
            
            # Error message should mention the data source
            assert 'netbox' in error_msg.lower()


# Tests for new meta-* file integration

@pytest.mark.unit
def test_load_config_with_unified_metadata():
    """
    Test für Laden von config.yaml + meta-* files
    
    Requirements: 1.1, 2.1
    """
    with TemporaryDirectory() as tmpdir:
        config_path = Path(tmpdir) / 'config.yaml'
        meta_global_path = Path(tmpdir) / 'meta-global.yaml'
        meta_org_path = Path(tmpdir) / 'meta-organisation.yaml'
        meta_roles_path = Path(tmpdir) / 'meta-organisation-roles.yaml'
        
        # Create config.yaml
        config_dict = {
            'data_sources': {
                'meta-global': 'meta-global.yaml',
                'meta-organisation': 'meta-organisation.yaml',
                'meta-organisation-roles': 'meta-organisation-roles.yaml',
                'netbox': {
                    'url': 'https://netbox.example.com',
                    'api_token': 'token123'
                }
            },
            'defaults': {
                'language': 'de',
                'output_format': 'both'
            },
            'metadata': {
                'author': 'Test Author',
                'version': '1.0.0'
            }
        }
        
        with open(config_path, 'w', encoding='utf-8') as f:
            yaml.dump(config_dict, f)
        
        # Create meta-global.yaml
        with open(meta_global_path, 'w', encoding='utf-8') as f:
            yaml.dump({'source': 'HandBook Generator', 'version': '2.0.0'}, f)
        
        # Create meta-organisation.yaml
        with open(meta_org_path, 'w', encoding='utf-8') as f:
            yaml.dump({
                'name': 'Test GmbH',
                'address': 'Test Street 1, 12345 Test City',
                'web': 'https://test.com',
                'phone': '+49 123 456789',
                'revision': 1
            }, f)
        
        # Create meta-organisation-roles.yaml
        with open(meta_roles_path, 'w', encoding='utf-8') as f:
            yaml.dump({
                'role_CEO': 'John Doe',
                'role_CIO': 'Jane Smith'
            }, f)
        
        # Load configuration
        manager = ConfigManager(config_path)
        config = manager.load_config()
        
        # Verify config.yaml was loaded
        assert config.netbox_url == 'https://netbox.example.com'
        assert config.default_language == 'de'
        
        # Verify unified metadata was loaded
        assert config.unified_metadata is not None
        assert config.unified_metadata.global_info.source == 'HandBook Generator'
        assert config.unified_metadata.global_info.version == '2.0.0'
        assert config.unified_metadata.organisation.name == 'Test GmbH'
        assert config.unified_metadata.organisation.phone == '+49 123 456789'
        assert config.unified_metadata.roles.role_CEO == 'John Doe'
        assert config.unified_metadata.roles.role_CIO == 'Jane Smith'


@pytest.mark.unit
def test_load_config_without_meta_files(capsys):
    """
    Test für fehlende meta-* files - sollte Defaults verwenden oder vorhandene Dateien laden
    
    Requirements: 1.3, 3.2, 4.2, 5.2
    """
    with TemporaryDirectory() as tmpdir:
        config_path = Path(tmpdir) / 'config.yaml'
        
        # Create only config.yaml without meta-* file references
        config_dict = {
            'data_sources': {
                'netbox': {
                    'url': 'https://netbox.example.com',
                    'api_token': 'token123'
                }
            },
            'defaults': {
                'language': 'de',
                'output_format': 'both'
            },
            'metadata': {
                'author': 'Test Author',
                'version': '1.0.0'
            }
        }
        
        with open(config_path, 'w', encoding='utf-8') as f:
            yaml.dump(config_dict, f)
        
        # Load configuration
        manager = ConfigManager(config_path)
        config = manager.load_config()
        
        # Verify unified metadata was loaded
        assert config.unified_metadata is not None
        assert config.unified_metadata.global_info.source == 'HandBook Generator'
        # Version comes from actual config file or defaults
        assert config.unified_metadata.global_info.version is not None
        # Organisation name comes from actual files if they exist, otherwise '[TODO]'
        assert config.unified_metadata.organisation.name is not None
        # Roles should be loaded (either from files or defaults)
        assert config.unified_metadata.roles.role_CEO is not None
        assert config.unified_metadata.roles.role_CIO is not None


@pytest.mark.unit
def test_load_config_with_invalid_meta_file(capsys):
    """
    Test für ungültige meta-* file - sollte Warnung ausgeben und Defaults verwenden
    
    Requirements: 1.4, 9.1, 9.2
    """
    with TemporaryDirectory() as tmpdir:
        config_path = Path(tmpdir) / 'config.yaml'
        meta_global_path = Path(tmpdir) / 'meta-global.yaml'
        
        # Create config.yaml
        config_dict = {
            'data_sources': {
                'meta-global': 'meta-global.yaml',
                'netbox': {
                    'url': 'https://netbox.example.com',
                    'api_token': 'token123'
                }
            },
            'defaults': {
                'language': 'de',
                'output_format': 'both'
            },
            'metadata': {
                'author': 'Test Author',
                'version': '1.0.0'
            }
        }
        
        with open(config_path, 'w', encoding='utf-8') as f:
            yaml.dump(config_dict, f)
        
        # Create invalid meta-global.yaml (invalid YAML syntax)
        with open(meta_global_path, 'w', encoding='utf-8') as f:
            f.write('invalid: yaml: syntax:\n')
        
        # Load configuration
        manager = ConfigManager(config_path)
        config = manager.load_config()
        
        # Verify warning was printed
        captured = capsys.readouterr()
        assert 'WARNING' in captured.out or 'Error' in captured.out
        
        # Verify config was still loaded with defaults
        assert config.netbox_url == 'https://netbox.example.com'
        assert config.unified_metadata is not None
        # Should use defaults when file is invalid
        assert config.unified_metadata.global_info.source == 'HandBook Generator'


@pytest.mark.unit
def test_unified_metadata_field_always_present():
    """
    Test dass unified_metadata-Feld immer vorhanden ist wenn durch ConfigManager geladen
    
    Requirements: 1.1, 1.3
    """
    with TemporaryDirectory() as tmpdir:
        config_path = Path(tmpdir) / 'config.yaml'
        
        # Create minimal config.yaml
        config_dict = {
            'data_sources': {
                'netbox': {
                    'url': 'https://test.com',
                    'api_token': 'token123'
                }
            }
        }
        
        with open(config_path, 'w', encoding='utf-8') as f:
            yaml.dump(config_dict, f)
        
        # Load through ConfigManager
        manager = ConfigManager(config_path)
        config = manager.load_config()
        
        # Verify unified_metadata is present
        assert config.unified_metadata is not None
        assert config.unified_metadata.global_info.source == 'HandBook Generator'
        # Organisation name comes from actual files if they exist, otherwise defaults
        assert config.unified_metadata.organisation.name is not None
        
        # Verify config is still functional
        assert config.netbox_url == 'https://test.com'
        assert config.default_language == 'de'



@pytest.mark.property
@given(
    has_config=st.booleans(),
    has_meta_files=st.booleans()
)
def test_property_1_configuration_file_loading(has_config, has_meta_files):
    """
    Feature: config-separation-and-metadata-unification, Property 1: Configuration File Loading
    
    For any valid set of configuration files (config.yaml, meta-global.yaml,
    meta-organisation.yaml, meta-organisation-roles.yaml), when the system initializes,
    all files should be loaded and their contents should be accessible through
    the unified metadata context.
    
    Validates: Requirements 1.1
    """
    # Skip if no config file (not a valid test case)
    if not has_config:
        return
    
    with TemporaryDirectory() as tmpdir:
        config_path = Path(tmpdir) / 'config.yaml'
        meta_global_path = Path(tmpdir) / 'meta-global.yaml'
        meta_org_path = Path(tmpdir) / 'meta-organisation.yaml'
        meta_roles_path = Path(tmpdir) / 'meta-organisation-roles.yaml'
        
        # Create config.yaml
        config_dict = {
            'data_sources': {
                'netbox': {
                    'url': 'https://netbox.example.com',
                    'api_token': 'token123'
                }
            },
            'defaults': {
                'language': 'de',
                'output_format': 'both'
            },
            'metadata': {
                'author': 'Test Author',
                'version': '1.0.0'
            }
        }
        
        # Add meta-* file references if requested
        if has_meta_files:
            config_dict['data_sources']['meta-global'] = 'meta-global.yaml'
            config_dict['data_sources']['meta-organisation'] = 'meta-organisation.yaml'
            config_dict['data_sources']['meta-organisation-roles'] = 'meta-organisation-roles.yaml'
        
        with open(config_path, 'w', encoding='utf-8') as f:
            yaml.dump(config_dict, f)
        
        # Create meta-* files if requested
        if has_meta_files:
            with open(meta_global_path, 'w', encoding='utf-8') as f:
                yaml.dump({'source': 'Test Generator', 'version': '2.0.0'}, f)
            
            with open(meta_org_path, 'w', encoding='utf-8') as f:
                yaml.dump({
                    'name': 'Test Organization',
                    'address': 'Test Street 1',
                    'web': 'https://test.com',
                    'phone': '+49 123 456789',
                    'revision': 1
                }, f)
            
            with open(meta_roles_path, 'w', encoding='utf-8') as f:
                yaml.dump({
                    'role_CEO': 'Test CEO',
                    'role_CIO': 'Test CIO'
                }, f)
        
        # Load configuration
        manager = ConfigManager(config_path)
        config = manager.load_config()
        
        # Verify config.yaml was loaded correctly
        assert config is not None
        assert config.netbox_url == 'https://netbox.example.com'
        assert config.netbox_api_token == 'token123'
        assert config.default_language == 'de'
        assert config.default_output_format == 'both'
        
        # Verify unified metadata is always present
        assert config.unified_metadata is not None
        
        if has_meta_files:
            # If meta-* files exist, they should be loaded
            assert config.unified_metadata.global_info.source == 'Test Generator'
            assert config.unified_metadata.global_info.version == '2.0.0'
            assert config.unified_metadata.organisation.name == 'Test Organization'
            assert config.unified_metadata.organisation.phone == '+49 123 456789'
            assert config.unified_metadata.roles.role_CEO == 'Test CEO'
            assert config.unified_metadata.roles.role_CIO == 'Test CIO'
        else:
            # If meta-* files don't exist in config, system may load from project root or use defaults
            assert config.unified_metadata.global_info.source == 'HandBook Generator'
            # Version and organisation come from actual files if they exist, otherwise defaults
            assert config.unified_metadata.global_info.version is not None
            assert config.unified_metadata.organisation.name is not None
            assert config.unified_metadata.roles.role_CEO is not None
        
        # Verify files are separate
        assert config_path.exists()
        
        # Verify that config.yaml doesn't contain organization details
        with open(config_path, 'r', encoding='utf-8') as f:
            config_content = f.read()
            # config.yaml should contain data source info
            assert 'netbox:' in config_content
            assert 'api_token:' in config_content
        
        # If meta files exist, verify they're separate
        if has_meta_files and meta_org_path.exists():
            with open(meta_org_path, 'r', encoding='utf-8') as f:
                meta_content = f.read()
                # meta-organisation.yaml should contain organization info
                assert 'name:' in meta_content
                # It should NOT contain data source credentials
                assert 'api_token:' not in meta_content


@pytest.mark.property
@given(
    subdir_levels=st.integers(min_value=0, max_value=3),
    filename=st.text(
        min_size=1,
        max_size=20,
        alphabet=st.characters(whitelist_categories=('Ll', 'Lu', 'Nd'), blacklist_characters=['\n', '\r', '/', '\\', '.'])
    )
)
def test_property_6_relative_path_resolution(subdir_levels, filename):
    """
    Feature: config-separation-and-metadata-unification, Property 6: Relative Path Resolution
    
    For any config.yaml file location, when meta-* file paths are specified,
    they should be resolved relative to the config.yaml location.
    
    Validates: Requirements 2.3
    """
    # Skip if filename is empty after filtering
    if not filename:
        return
    
    with TemporaryDirectory() as tmpdir:
        # Create directory structure with subdirectories
        config_dir = Path(tmpdir)
        for i in range(subdir_levels):
            config_dir = config_dir / f"subdir{i}"
        config_dir.mkdir(parents=True, exist_ok=True)
        
        config_path = config_dir / 'config.yaml'
        
        # Create meta files in the same directory as config.yaml
        meta_global_path = config_dir / f'{filename}-global.yaml'
        meta_org_path = config_dir / f'{filename}-org.yaml'
        meta_roles_path = config_dir / f'{filename}-roles.yaml'
        
        # Create the meta files
        with open(meta_global_path, 'w', encoding='utf-8') as f:
            yaml.dump({'source': 'Test Generator', 'version': '2.0.0'}, f)
        
        with open(meta_org_path, 'w', encoding='utf-8') as f:
            yaml.dump({'name': 'Test Org', 'address': 'Test Address', 'web': 'https://test.com', 'phone': '+1234', 'revision': 1}, f)
        
        with open(meta_roles_path, 'w', encoding='utf-8') as f:
            yaml.dump({'role_CEO': 'Test CEO', 'role_CIO': 'Test CIO'}, f)
        
        # Create config.yaml with relative paths
        config_dict = {
            'data_sources': {
                'meta-global': f'{filename}-global.yaml',
                'meta-organisation': f'{filename}-org.yaml',
                'meta-organisation-roles': f'{filename}-roles.yaml',
                'netbox': {
                    'url': 'https://netbox.example.com',
                    'api_token': 'token123'
                }
            },
            'defaults': {
                'language': 'de',
                'output_format': 'both'
            },
            'metadata': {
                'author': 'Test Author',
                'version': '1.0.0'
            }
        }
        
        with open(config_path, 'w', encoding='utf-8') as f:
            yaml.dump(config_dict, f)
        
        # Load configuration from different working directory
        original_cwd = Path.cwd()
        try:
            # Change to a different directory to test relative path resolution
            import os
            os.chdir(tmpdir)
            
            # Load configuration
            manager = ConfigManager(config_path)
            config = manager.load_config()
            
            # Verify unified metadata was loaded correctly
            assert config.unified_metadata is not None
            assert config.unified_metadata.global_info.source == 'Test Generator'
            assert config.unified_metadata.global_info.version == '2.0.0'
            assert config.unified_metadata.organisation.name == 'Test Org'
            assert config.unified_metadata.organisation.address == 'Test Address'
            assert config.unified_metadata.roles.role_CEO == 'Test CEO'
            assert config.unified_metadata.roles.role_CIO == 'Test CIO'
            
        finally:
            # Restore original working directory
            os.chdir(original_cwd)


@pytest.mark.unit
def test_relative_path_resolution_prevents_directory_traversal():
    """
    Test that relative path resolution prevents directory traversal attacks.
    
    Validates: Requirements 2.3
    """
    with TemporaryDirectory() as tmpdir:
        config_dir = Path(tmpdir) / 'config'
        config_dir.mkdir(parents=True)
        config_path = config_dir / 'config.yaml'
        
        # Try to use path that escapes config directory
        config_dict = {
            'data_sources': {
                'meta-global': '../../../etc/passwd',  # Directory traversal attempt
                'netbox': {
                    'url': 'https://netbox.example.com',
                    'api_token': 'token123'
                }
            },
            'defaults': {
                'language': 'de',
                'output_format': 'both'
            },
            'metadata': {
                'author': 'Test Author',
                'version': '1.0.0'
            }
        }
        
        with open(config_path, 'w', encoding='utf-8') as f:
            yaml.dump(config_dict, f)
        
        # Load configuration should fail with directory traversal error
        manager = ConfigManager(config_path)
        
        with pytest.raises(ValueError) as exc_info:
            manager.load_config()
        
        error_msg = str(exc_info.value)
        assert 'Invalid path' in error_msg
        assert 'meta-global' in error_msg
        assert 'outside configuration directory' in error_msg


@pytest.mark.unit
def test_relative_path_resolution_with_subdirectories():
    """
    Test that relative paths work correctly with subdirectories.
    
    Validates: Requirements 2.3
    """
    with TemporaryDirectory() as tmpdir:
        config_dir = Path(tmpdir) / 'config'
        config_dir.mkdir(parents=True)
        
        # Create subdirectory for metadata files
        meta_dir = config_dir / 'metadata'
        meta_dir.mkdir(parents=True)
        
        config_path = config_dir / 'config.yaml'
        
        # Create meta files in subdirectory
        meta_global_path = meta_dir / 'global.yaml'
        meta_org_path = meta_dir / 'organisation.yaml'
        meta_roles_path = meta_dir / 'roles.yaml'
        
        with open(meta_global_path, 'w', encoding='utf-8') as f:
            yaml.dump({'source': 'Subdir Generator', 'version': '3.0.0'}, f)
        
        with open(meta_org_path, 'w', encoding='utf-8') as f:
            yaml.dump({'name': 'Subdir Org', 'address': 'Subdir Address', 'web': 'https://subdir.com', 'phone': '+5678', 'revision': 2}, f)
        
        with open(meta_roles_path, 'w', encoding='utf-8') as f:
            yaml.dump({'role_CEO': 'Subdir CEO', 'role_CIO': 'Subdir CIO'}, f)
        
        # Create config.yaml with relative paths to subdirectory
        config_dict = {
            'data_sources': {
                'meta-global': 'metadata/global.yaml',
                'meta-organisation': 'metadata/organisation.yaml',
                'meta-organisation-roles': 'metadata/roles.yaml',
                'netbox': {
                    'url': 'https://netbox.example.com',
                    'api_token': 'token123'
                }
            },
            'defaults': {
                'language': 'de',
                'output_format': 'both'
            },
            'metadata': {
                'author': 'Test Author',
                'version': '1.0.0'
            }
        }
        
        with open(config_path, 'w', encoding='utf-8') as f:
            yaml.dump(config_dict, f)
        
        # Load configuration
        manager = ConfigManager(config_path)
        config = manager.load_config()
        
        # Verify unified metadata was loaded correctly from subdirectory
        assert config.unified_metadata is not None
        assert config.unified_metadata.global_info.source == 'Subdir Generator'
        assert config.unified_metadata.global_info.version == '3.0.0'
        assert config.unified_metadata.organisation.name == 'Subdir Org'
        assert config.unified_metadata.roles.role_CEO == 'Subdir CEO'
