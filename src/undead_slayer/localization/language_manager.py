"""Language manager for the game."""

import gettext
import os

from undead_slayer.config.config_manager import config_manager


class Localization:
    def __init__(self, default_locale: str):
        self.locales_directory = os.path.join(
            os.path.dirname(__file__), "..", "locales"
        )
        self.set_language(default_locale)

    def set_language(self, locale: str):
        """Set the language for the game."""
        self.language = gettext.translation(
            domain="messages",
            localedir=self.locales_directory,
            languages=[locale],
            fallback=True,
        )
        self.language.install()

    def get_available_languages(self):
        """Return a list of available languages based on locales directory."""
        return [
            name
            for name in os.listdir(self.locales_directory)
            if os.path.isdir(os.path.join(self.locales_directory, name))
        ]


# Instantiate a global localization object
localization = Localization(default_locale=config_manager.get_config().locale)
