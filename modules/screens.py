import os

from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal

from modules.bar_styles.silver_blade import SilverBlades
from modules.colors.github_dark import GithubDark

colors = GithubDark()

screens = SilverBlades(colors=colors).screens
