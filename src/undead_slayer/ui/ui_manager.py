"""User Interface (UI) manager for the game."""

from undead_slayer.config.config_manager import config_manager
from undead_slayer.enums import UI
from undead_slayer.ui.cli.cli import CLI
from undead_slayer.ui.gui.gui import GUI
from undead_slayer.ui.tui.tui import TUI


def get_default_ui() -> UI:
    """Return the default user interface (UI) for the game."""
    return UI(config_manager.get_config().default_ui)


def launch_ui(ui: UI) -> None:
    """Launch the specified user interface (UI).

    Parameters:
    -----
        ui (UI): The user interface (UI) to launch.
    """
    if ui == UI.CLI:
        print("CLI")
        CLI()
    elif ui == UI.TUI:
        print("TUI")
        TUI()
    elif ui == UI.GUI:
        print("GUI")
        GUI()
