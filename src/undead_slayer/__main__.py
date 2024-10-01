"""The main entry point for the game."""

from typing import Annotated

import typer

from undead_slayer.localization.language_manager import localization
from undead_slayer.ui.ui_manager import UI, get_default_ui, launch_ui

_ = localization.language.gettext
app = typer.Typer(help=_("An RPG Game!"), no_args_is_help=True)


@app.command(
    short_help=_("Play the game."),
    help=_(
        """Play the game, with either a simple command-line (CLI),
        text (TUI), or graphical user interface (GUI)."""
    ),
)
def play(
    ui: Annotated[
        UI | None,
        typer.Argument(
            help=_("The user interface to use. Uses the default if not provided."),
            show_default=False,
            case_sensitive=False,
        ),
    ] = None,
):
    if ui is None:
        ui = get_default_ui()
    launch_ui(ui)


@app.command()
def foo(): ...


if __name__ == "__main__":
    app()
