from enum import StrEnum


class UI(StrEnum):
    CLI = "cli"
    TUI = "tui"
    GUI = "gui"


class Theme(StrEnum):
    LIGHT = "light"
    DARK = "dark"


class Difficulty(StrEnum):
    EASY = "easy"
    NORMAL = "normal"
    HARD = "hard"
    INSANE = "insane"
    NIGHTMARE = "nightmare"
