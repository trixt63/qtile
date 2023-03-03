import os

from libqtile import bar
from .widgets import *
from libqtile.config import Screen
from modules.keys import terminal

from modules.bar_styles.silver_blade2 import SilverBlades2
from modules.bar_styles.silver_blade1 import SilverBlades1
from modules.bar_styles.simple_slash import SimpleSlash
from modules.bar_styles.simple_slash_translucent import SimpleSlashTranslucent
from modules.colors.github_dark import GithubDark
from modules.colors.nord import Nord
from modules.colors.space_gray import SpaceGray

# colors = Nord().colors
colors = SpaceGray().colors

# screens = SilverBlades1(colors=colors).screens
screens = SimpleSlash(colors=colors).screens
