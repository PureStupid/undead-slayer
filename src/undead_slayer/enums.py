from enum import StrEnum


class UI(StrEnum):
    """The user interfaces available for the game."""

    CLI = "cli"
    TUI = "tui"
    GUI = "gui"


class Theme(StrEnum):
    """The themes available for the game."""

    LIGHT = "light"
    DARK = "dark"


class Difficulty(StrEnum):
    """The difficulties available for the game."""

    EASY = "easy"
    NORMAL = "normal"
    HARD = "hard"
    INSANE = "insane"
    NIGHTMARE = "nightmare"
