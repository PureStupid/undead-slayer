"""Configuration manager for the game."""

from dataclasses import dataclass
from pathlib import Path

import yaml
from pydantic import BaseModel

from undead_slayer.enums import UI, Theme
from undead_slayer.utils.locations import config_file


# TODO: Add more configuration options
class AppConfig(BaseModel):
    """Configuration for the game."""

    locale: str = "en-GB"
    default_ui: str = UI.CLI.value
    sound_volume: float = 0.5
    music_volume: float = 0.5
    theme: str = Theme.LIGHT.value


@dataclass
class ConfigManager:
    config_file: Path

    def __post_init__(self):
        self.config: AppConfig = (
            self.load_config() if self.config_file.exists() else self.create_config()
        )

    def load_config(self) -> AppConfig:
        """Load the configuration from the config file."""
        with open(self.config_file) as file:
            config_data = yaml.safe_load(file)

        # If the file is empty, create a new configuration
        if config_data is None:
            return self.create_config()
        return AppConfig(**config_data)

    def create_config(self):
        """Create a new configuration file with the default values."""
        with open(self.config_file, "w") as file:
            yaml.safe_dump(AppConfig().model_dump(), file)
        return AppConfig()

    def get_config(self) -> AppConfig:
        """Return the current configuration."""
        return self.config

    def update_config(self, config: AppConfig):
        """Update the configuration with the new values."""
        self.config = config
        with open(self.config_file, "w") as file:
            yaml.safe_dump(config.model_dump(), file)

    def reset_config(self):
        """Reset the configuration to the default values."""
        self.config = self.create_config()


config_manager = ConfigManager(config_file())
