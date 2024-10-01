from unittest.mock import patch

import pytest
from typer.testing import CliRunner

from undead_slayer.__main__ import app
from undead_slayer.enums import UI

runner = CliRunner()


@pytest.mark.parametrize(
    "ui",
    [
        UI.CLI,
        UI.TUI,
        UI.GUI,
    ],
)
class TestMain:
    @staticmethod
    def test_play_with_default_ui(ui: UI):
        """Test the `play` command with the default UI.

        Parameters:
        -----------
        ui : UI
            The default user interface.
        """
        with (
            patch("undead_slayer.__main__.get_default_ui") as mock_get_default_ui,
            patch("undead_slayer.__main__.launch_ui") as mock_launch_ui,
        ):
            mock_get_default_ui.return_value = ui

            result = runner.invoke(app, ["play"])

            assert result.exit_code == 0
            mock_get_default_ui.assert_called_once()
            mock_launch_ui.assert_called_once_with(ui)

    @staticmethod
    def test_play_with_specific_ui(ui: UI):
        """Test the `play` command with a specific UI.

        Parameters:
        -----------
        ui : UI
            The specific user interface.
        """
        with patch("undead_slayer.__main__.launch_ui") as mock_launch_ui:
            result = runner.invoke(app, ["play", ui.value])

            assert result.exit_code == 0
            mock_launch_ui.assert_called_once_with(ui)
