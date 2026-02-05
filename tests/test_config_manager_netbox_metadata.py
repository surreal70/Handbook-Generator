"""
Unit tests for ConfigManager NetBox metadata loading

Author: Andreas Huemmer [andreas.huemmer@adminsend.de]
Copyright: 2025
"""

import pytest
import yaml
from pathlib import Path
from src.config_manager import ConfigManager


class TestConfigManagerNetBoxMetadata:
    """Test suite for ConfigManager NetBox metadata loading."""
    
    @pytest.fixture
    def temp_config_dir(self, tmp_path):
        """Create temporary config directory."""
        config_dir = tmp_path / "config"
        config_dir.mkdir()
        return config_dir
    
    @pytest.fixture
    def sample_netbox_metadata(self):
        """Sample NetBox metadata for testing."""
        return {
            'contacts': {
                'ciso': {
                    'name': 'John Security',
                    'email': 'john.security@example.com'
                }
            },
            'devices': {
                'firewall': {
                    'name': 'fw-01',
                    'ip': '192.168.1.1'
                }
            },
            'sites': {
                'primary': {
                    'name': 'Headquarters'
                }
            }
        }
    
    def test_load_netbox_metadata_success(self, temp_config_dir, sample_netbox_metadata):
        """Test successful loading of NetBox metadata."""
        # Create metadata-netbox.yaml file
        netbox_metadata_path = temp_config_dir / "metadata-netbox.yaml"
        with open(netbox_metadata_path, 'w', encoding='utf-8') as f:
            yaml.dump(sample_netbox_metadata, f)
        
        # Create config manager
        config_path = temp_config_dir / "config.yaml"
        config_manager = ConfigManager(config_path)
        
        # Load NetBox metadata
        result = config_manager.load_netbox_metadata(netbox_metadata_path)
        
        # Verify result
        assert result is not None
        assert result == sample_netbox_metadata
        assert 'contacts' in result
        assert 'devices' in result
        assert 'sites' in result
    
    def test_load_netbox_metadata_file_not_found(self, temp_config_dir, capsys):
        """Test loading NetBox metadata when file doesn't exist."""
        # Create config manager
        config_path = temp_config_dir / "config.yaml"
        config_manager = ConfigManager(config_path)
        
        # Try to load non-existent file
        netbox_metadata_path = temp_config_dir / "metadata-netbox.yaml"
        result = config_manager.load_netbox_metadata(netbox_metadata_path)
        
        # Verify result is None
        assert result is None
        
        # Verify info message was printed
        captured = capsys.readouterr()
        assert "metadata-netbox.yaml not found" in captured.out
        assert "NetBox metadata will not be available" in captured.out
    
    def test_load_netbox_metadata_default_path(self, temp_config_dir, sample_netbox_metadata):
        """Test loading NetBox metadata from default path (project root)."""
        # Create config manager
        config_path = temp_config_dir / "config.yaml"
        config_manager = ConfigManager(config_path)
        
        # Create metadata-netbox.yaml in project root
        netbox_metadata_path = config_manager.project_root / "metadata-netbox.yaml"
        with open(netbox_metadata_path, 'w', encoding='utf-8') as f:
            yaml.dump(sample_netbox_metadata, f)
        
        try:
            # Load NetBox metadata without specifying path
            result = config_manager.load_netbox_metadata()
            
            # Verify result
            assert result is not None
            assert result == sample_netbox_metadata
        finally:
            # Clean up
            if netbox_metadata_path.exists():
                netbox_metadata_path.unlink()
    
    def test_load_netbox_metadata_invalid_yaml(self, temp_config_dir):
        """Test loading NetBox metadata with invalid YAML syntax."""
        # Create invalid YAML file
        netbox_metadata_path = temp_config_dir / "metadata-netbox.yaml"
        with open(netbox_metadata_path, 'w', encoding='utf-8') as f:
            f.write("invalid: yaml: syntax: [")
        
        # Create config manager
        config_path = temp_config_dir / "config.yaml"
        config_manager = ConfigManager(config_path)
        
        # Try to load invalid YAML
        with pytest.raises(yaml.YAMLError, match="Invalid YAML syntax"):
            config_manager.load_netbox_metadata(netbox_metadata_path)
    
    def test_load_netbox_metadata_empty_file(self, temp_config_dir, capsys):
        """Test loading NetBox metadata from empty file."""
        # Create empty YAML file
        netbox_metadata_path = temp_config_dir / "metadata-netbox.yaml"
        with open(netbox_metadata_path, 'w', encoding='utf-8') as f:
            f.write("")
        
        # Create config manager
        config_path = temp_config_dir / "config.yaml"
        config_manager = ConfigManager(config_path)
        
        # Load empty file
        result = config_manager.load_netbox_metadata(netbox_metadata_path)
        
        # Verify result is None
        assert result is None
        
        # Verify warning message was printed
        captured = capsys.readouterr()
        assert "NetBox metadata file is empty" in captured.out
    
    def test_load_netbox_metadata_invalid_structure(self, temp_config_dir):
        """Test loading NetBox metadata with invalid structure."""
        # Create YAML file with invalid structure (not a dict)
        netbox_metadata_path = temp_config_dir / "metadata-netbox.yaml"
        with open(netbox_metadata_path, 'w', encoding='utf-8') as f:
            yaml.dump(["list", "instead", "of", "dict"], f)
        
        # Create config manager
        config_path = temp_config_dir / "config.yaml"
        config_manager = ConfigManager(config_path)
        
        # Try to load invalid structure
        with pytest.raises(ValueError, match="Invalid NetBox metadata structure"):
            config_manager.load_netbox_metadata(netbox_metadata_path)
    
    def test_load_netbox_metadata_with_nested_structure(self, temp_config_dir):
        """Test loading NetBox metadata with deeply nested structure."""
        # Create complex nested metadata
        complex_metadata = {
            'contacts': {
                'ciso': {
                    'name': 'John Security',
                    'email': 'john.security@example.com',
                    'details': {
                        'department': 'IT Security',
                        'location': {
                            'building': 'HQ',
                            'floor': 3
                        }
                    }
                }
            },
            'devices': {
                'network': {
                    'firewall': {
                        'name': 'fw-01',
                        'specs': {
                            'model': 'Cisco ASA',
                            'ports': 24
                        }
                    }
                }
            }
        }
        
        # Create metadata-netbox.yaml file
        netbox_metadata_path = temp_config_dir / "metadata-netbox.yaml"
        with open(netbox_metadata_path, 'w', encoding='utf-8') as f:
            yaml.dump(complex_metadata, f)
        
        # Create config manager
        config_path = temp_config_dir / "config.yaml"
        config_manager = ConfigManager(config_path)
        
        # Load NetBox metadata
        result = config_manager.load_netbox_metadata(netbox_metadata_path)
        
        # Verify result
        assert result is not None
        assert result == complex_metadata
        assert result['contacts']['ciso']['details']['location']['floor'] == 3
        assert result['devices']['network']['firewall']['specs']['ports'] == 24
