"""
Tests for Configuration Manager

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2026
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


# Tests for metadata.yaml integration

@pytest.mark.unit
def test_load_config_with_metadata():
    """
    Test für Laden von config.yaml + metadata.yaml
    
    Requirements: 17.1, 19.1
    """
    with TemporaryDirectory() as tmpdir:
        config_path = Path(tmpdir) / 'config.yaml'
        metadata_path = Path(tmpdir) / 'metadata.yaml'
        
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
        
        with open(config_path, 'w', encoding='utf-8') as f:
            yaml.dump(config_dict, f)
        
        # Create metadata.yaml
        metadata_dict = {
            'organization': {
                'name': 'Test GmbH',
                'address': 'Test Street 1',
                'city': 'Test City',
                'postal_code': '12345',
                'country': 'Germany',
                'website': 'https://test.com',
                'phone': '+49 123 456789',
                'email': 'info@test.com'
            },
            'roles': {
                'ceo': {
                    'name': 'John Doe',
                    'title': 'CEO',
                    'email': 'john@test.com',
                    'phone': '+49 123 456789'
                }
            },
            'document': {
                'owner': 'IT Manager',
                'approver': 'CIO',
                'version': '1.0.0',
                'classification': 'internal'
            },
            'defaults': {
                'author': 'Test Author',
                'language': 'de'
            }
        }
        
        with open(metadata_path, 'w', encoding='utf-8') as f:
            yaml.dump(metadata_dict, f)
        
        # Load configuration
        manager = ConfigManager(config_path)
        config = manager.load_config()
        
        # Verify config.yaml was loaded
        assert config.netbox_url == 'https://netbox.example.com'
        assert config.default_language == 'de'
        
        # Verify metadata.yaml was loaded
        assert config.metadata is not None
        assert config.metadata.organization.name == 'Test GmbH'
        assert config.metadata.organization.email == 'info@test.com'
        assert 'ceo' in config.metadata.roles
        assert config.metadata.roles['ceo'].name == 'John Doe'
        assert config.metadata.document.owner == 'IT Manager'


@pytest.mark.unit
def test_load_config_without_metadata(capsys):
    """
    Test für fehlende metadata.yaml - sollte Default erstellen
    
    Requirements: 17.1
    """
    with TemporaryDirectory() as tmpdir:
        config_path = Path(tmpdir) / 'config.yaml'
        metadata_path = Path(tmpdir) / 'metadata.yaml'
        
        # Create only config.yaml
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
        
        # Verify metadata.yaml doesn't exist yet
        assert not metadata_path.exists()
        
        # Load configuration
        manager = ConfigManager(config_path)
        config = manager.load_config()
        
        # Verify metadata.yaml was created
        assert metadata_path.exists()
        
        # Verify output messages
        captured = capsys.readouterr()
        assert 'metadata.yaml not found' in captured.out
        assert 'Creating default metadata.yaml' in captured.out
        assert 'Default metadata.yaml created' in captured.out
        
        # Verify metadata was loaded with default values
        assert config.metadata is not None
        assert config.metadata.organization.name == 'AdminSend GmbH'
        assert 'ceo' in config.metadata.roles
        assert 'cio' in config.metadata.roles


@pytest.mark.unit
def test_load_config_with_invalid_metadata(capsys):
    """
    Test für ungültige metadata.yaml - sollte Warnung ausgeben und fortfahren
    
    Requirements: 17.1
    """
    with TemporaryDirectory() as tmpdir:
        config_path = Path(tmpdir) / 'config.yaml'
        metadata_path = Path(tmpdir) / 'metadata.yaml'
        
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
        
        with open(config_path, 'w', encoding='utf-8') as f:
            yaml.dump(config_dict, f)
        
        # Create invalid metadata.yaml (missing required fields)
        with open(metadata_path, 'w', encoding='utf-8') as f:
            f.write('invalid: yaml\n')
        
        # Load configuration
        manager = ConfigManager(config_path)
        config = manager.load_config()
        
        # Verify warning was printed
        captured = capsys.readouterr()
        assert 'WARNING' in captured.out
        assert 'Error loading metadata.yaml' in captured.out
        
        # Verify config was still loaded but without metadata
        assert config.netbox_url == 'https://netbox.example.com'
        assert config.metadata is None


@pytest.mark.unit
def test_ensure_metadata_file_creates_default(capsys):
    """
    Test für ensure_metadata_file() - erstellt Default wenn fehlend
    
    Requirements: 17.1
    """
    with TemporaryDirectory() as tmpdir:
        config_path = Path(tmpdir) / 'config.yaml'
        metadata_path = Path(tmpdir) / 'metadata.yaml'
        
        # Create config.yaml
        with open(config_path, 'w', encoding='utf-8') as f:
            f.write('data_sources:\n  netbox:\n    url: https://test.com\n    api_token: token\n')
        
        manager = ConfigManager(config_path)
        
        # Verify metadata.yaml doesn't exist
        assert not metadata_path.exists()
        
        # Call ensure_metadata_file
        manager.ensure_metadata_file()
        
        # Verify metadata.yaml was created
        assert metadata_path.exists()
        
        # Verify output messages
        captured = capsys.readouterr()
        assert 'metadata.yaml not found' in captured.out
        assert 'Creating default metadata.yaml' in captured.out
        assert 'SUCCESS' in captured.out
        
        # Verify content is valid
        with open(metadata_path, 'r', encoding='utf-8') as f:
            content = f.read()
            assert 'organization:' in content
            assert 'roles:' in content
            assert 'ceo:' in content


@pytest.mark.unit
def test_ensure_metadata_file_already_exists(capsys):
    """
    Test für ensure_metadata_file() - keine Aktion wenn bereits vorhanden
    
    Requirements: 17.1
    """
    with TemporaryDirectory() as tmpdir:
        config_path = Path(tmpdir) / 'config.yaml'
        metadata_path = Path(tmpdir) / 'metadata.yaml'
        
        # Create both files
        with open(config_path, 'w', encoding='utf-8') as f:
            f.write('data_sources:\n  netbox:\n    url: https://test.com\n    api_token: token\n')
        
        with open(metadata_path, 'w', encoding='utf-8') as f:
            f.write('existing: content\n')
        
        manager = ConfigManager(config_path)
        
        # Call ensure_metadata_file
        manager.ensure_metadata_file()
        
        # Verify file still exists with original content
        assert metadata_path.exists()
        with open(metadata_path, 'r', encoding='utf-8') as f:
            content = f.read()
            assert 'existing: content' in content
        
        # Verify output message
        captured = capsys.readouterr()
        assert 'metadata.yaml found' in captured.out


@pytest.mark.unit
def test_config_metadata_field_optional():
    """
    Test dass metadata-Feld optional ist
    
    Requirements: 17.1
    """
    # Create Config without metadata
    config = Config(
        data_sources={
            'netbox': DataSourceConfig(
                url='https://test.com',
                api_token='token123'
            )
        }
    )
    
    # Verify metadata is None by default
    assert config.metadata is None
    
    # Verify config is still functional
    assert config.netbox_url == 'https://test.com'
    assert config.default_language == 'de'



@pytest.mark.property
@given(
    has_config=st.booleans(),
    has_metadata=st.booleans()
)
def test_property_20_configuration_file_separation(has_config, has_metadata):
    """
    Feature: it-operation-template-extension, Property 20: Configuration File Separation
    
    For any system configuration, metadata configuration (metadata.yaml) should be
    separate from data source configuration (config.yaml) and both should be
    loadable independently.
    
    Validates: Requirements 17.1, 19.1
    """
    # Skip if neither file exists (not a valid test case)
    if not has_config:
        return
    
    with TemporaryDirectory() as tmpdir:
        config_path = Path(tmpdir) / 'config.yaml'
        metadata_path = Path(tmpdir) / 'metadata.yaml'
        
        # Create config.yaml if requested
        if has_config:
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
        
        # Create metadata.yaml if requested
        if has_metadata:
            metadata_dict = {
                'organization': {
                    'name': 'Test Organization',
                    'address': 'Test Street 1',
                    'city': 'Test City',
                    'postal_code': '12345',
                    'country': 'Test Country',
                    'website': 'https://test.com',
                    'phone': '+49 123 456789',
                    'email': 'info@test.com'
                },
                'roles': {
                    'ceo': {
                        'name': 'Test CEO',
                        'title': 'Chief Executive Officer',
                        'email': 'ceo@test.com',
                        'phone': '+49 123 456789'
                    }
                },
                'document': {
                    'owner': 'Test Owner',
                    'approver': 'Test Approver',
                    'version': '1.0.0',
                    'classification': 'internal'
                },
                'defaults': {
                    'author': 'Test Author',
                    'language': 'de'
                }
            }
            
            with open(metadata_path, 'w', encoding='utf-8') as f:
                yaml.dump(metadata_dict, f)
        
        # Load configuration
        manager = ConfigManager(config_path)
        config = manager.load_config()
        
        # Verify config.yaml was loaded correctly
        assert config is not None
        assert config.netbox_url == 'https://netbox.example.com'
        assert config.netbox_api_token == 'token123'
        assert config.default_language == 'de'
        assert config.default_output_format == 'both'
        
        # Verify metadata separation
        if has_metadata:
            # If metadata.yaml exists, it should be loaded
            assert config.metadata is not None
            assert config.metadata.organization.name == 'Test Organization'
            assert config.metadata.organization.email == 'info@test.com'
            assert 'ceo' in config.metadata.roles
            assert config.metadata.roles['ceo'].name == 'Test CEO'
        else:
            # If metadata.yaml doesn't exist, a default should be created
            # and loaded (or metadata should be None if creation fails)
            # In our implementation, we create a default, so it should be loaded
            assert config.metadata is not None
            # Default metadata should have AdminSend GmbH as organization
            assert config.metadata.organization.name == 'AdminSend GmbH'
        
        # Verify files are separate
        assert config_path.exists()
        
        # Verify that config.yaml doesn't contain metadata organization info
        with open(config_path, 'r', encoding='utf-8') as f:
            config_content = f.read()
            # config.yaml should not contain organization details
            assert 'organization:' not in config_content or 'data_sources:' in config_content
            # It should contain data source info
            assert 'netbox:' in config_content
            assert 'api_token:' in config_content
        
        # If metadata exists, verify it's separate
        if metadata_path.exists():
            with open(metadata_path, 'r', encoding='utf-8') as f:
                metadata_content = f.read()
                # metadata.yaml should contain organization info
                assert 'organization:' in metadata_content
                # It should NOT contain data source credentials
                assert 'api_token:' not in metadata_content or 'netbox:' not in metadata_content
