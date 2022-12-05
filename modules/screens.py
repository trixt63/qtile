import os

from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal

from modules.bar_styles.silver_blade2 import SilverBlades2
from modules.bar_styles.silver_blade1 import SilverBlades1
from modules.colors.github_dark import GithubDark

colors = GithubDark()

screens = SilverBlades2(colors=colors).screens
