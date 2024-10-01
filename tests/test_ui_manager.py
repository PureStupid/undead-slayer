from unittest.mock import patch

import pytest

from undead_slayer.ui.cli.cli import CLI
from undead_slayer.ui.gui.gui import GUI
from undead_slayer.ui.tui.tui import TUI
from undead_slayer.ui.ui_manager import UI, launch_ui


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
