from pathlib import Path

import pytest
import yaml

from undead_slayer.config.config_manager import AppConfig, ConfigManager


@pytest.fixture
def config_file_path(tmp_path: Path):
    return tmp_path / "config.yaml"


@pytest.fixture
def default_config():
    return AppConfig()


def test_create_config(config_file_path: Path, default_config: AppConfig):
    """Test creating a new configuration file with the default values."""
    config_manager = ConfigManager(config_file=config_file_path)
    assert config_manager.get_config() == default_config
    assert config_file_path.exists()


def test_load_config(config_file_path: Path, default_config: AppConfig):
    """Test loading the configuration from the config file."""
    config_data = default_config.model_dump()
    with open(config_file_path, "w") as file:
        yaml.safe_dump(config_data, file)

    config_manager = ConfigManager(config_file=config_file_path)
    assert config_manager.get_config() == default_config


def test_update_config(config_file_path: Path):
    """Test updating the configuration with the new values."""
    config_manager = ConfigManager(config_file=config_file_path)
    new_config = AppConfig(locale="fr-FR", sound_volume=0.8)
    config_manager.update_config(new_config)

    assert config_manager.get_config() == new_config

    with open(config_file_path) as file:
        config_data = yaml.safe_load(file)
    assert config_data == new_config.model_dump()


def test_reset_config(config_file_path: Path, default_config: AppConfig):
    """Test resetting the configuration to the default values."""
    config_manager = ConfigManager(config_file=config_file_path)
    new_config = AppConfig(locale="fr-FR", sound_volume=0.8)
    config_manager.update_config(new_config)

    config_manager.reset_config()
    assert config_manager.get_config() == default_config

    with open(config_file_path) as file:
        config_data = yaml.safe_load(file)
    assert config_data == default_config.model_dump()
