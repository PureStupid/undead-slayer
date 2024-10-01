"""Utilities for determining the location of application data and config files."""

from pathlib import Path

from xdg_base_dirs import xdg_config_home, xdg_data_home


def _undead_slayer_directory(root: Path) -> Path:
    """Return (possibly creating) the undead_slayer directory under the given root."""
    directory = root / "undead_slayer"
    directory.mkdir(exist_ok=True, parents=True)
    return directory


def data_directory() -> Path:
    """Return (possibly creating) the application data directory."""
    return _undead_slayer_directory(xdg_data_home())


def config_directory() -> Path:
    """Return (possibly creating) the application config directory."""
    return _undead_slayer_directory(xdg_config_home())


def config_file() -> Path:
    """Return the path to the config file."""
    return config_directory() / "config.yaml"
