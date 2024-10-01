from unittest.mock import patch

import pytest

from undead_slayer.config.config_manager import ConfigManager
from undead_slayer.enums import UI
from undead_slayer.ui.cli.cli import CLI
from undead_slayer.ui.gui.gui import GUI
from undead_slayer.ui.tui.tui import TUI
from undead_slayer.ui.ui_manager import get_default_ui, launch_ui
from undead_slayer.utils.locations import config_file


def test_get_default_ui():
    """
    Test the `get_default_ui` function.
    """
    with patch.object(
        ConfigManager, "get_config", return_value=ConfigManager(config_file()).config
    ) as mock_get_config:
        mock_get_config.return_value.default_ui = UI.CLI.value
        assert get_default_ui() == UI.CLI

        mock_get_config.return_value.default_ui = UI.TUI.value
        assert get_default_ui() == UI.TUI

        mock_get_config.return_value.default_ui = UI.GUI.value
        assert get_default_ui() == UI.GUI


@pytest.mark.parametrize(
    "ui, expected_class",
    [
        (UI.CLI, CLI),
        (UI.TUI, TUI),
        (UI.GUI, GUI),
    ],
)
def test_launch_ui(ui: UI, expected_class: type):
    """
    Test the `launch_ui` function.

    Parameters:
    -----------
    ui : UI
        The user interface to be launched.
    expected_class : class
        The expected class to be instantiated.
    """
    with patch.object(expected_class, "__init__", return_value=None) as mock_init:
        launch_ui(ui)
        mock_init.assert_called_once()
